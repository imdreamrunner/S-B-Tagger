__author__ = "Xinzi Zhou"
__email__ = "imdreamrunner@gmail.com"


import logging
import datetime
from . import db

log = logging.getLogger(__name__)


SELECT_OPTIONS = """
    SELECT `id`, `display` FROM `option`;
"""

SELECT_ITEM = """
    SELECT `id`, `content` FROM `item` WHERE `id` = %s;
"""

SELECT_RANDOM_ITEM = """
    SELECT i.`id`, i.`content` FROM `item` AS i
      JOIN (SELECT CEIL(RAND() * (SELECT MAX(`id`) FROM `item` WHERE `tag` = 0)) AS id) AS r
     WHERE i.`tag` = 0 AND i.`id` >= r.`id` LIMIT 1;
"""

COUNT_OPTION_VOTE = """
    SELECT count(*) FROM `vote` WHERE `item` = %s AND `option` = %s
"""

VOTE_FOR_ITEM = """
    INSERT INTO `vote` (`item`, `option`, `create_time`) VALUES (%s, %s, %s);
"""

UPDATE_ITEM = """
    UPDATE `item` SET `tag` = %s WHERE `id` = %s
"""


def get_options():
    """
    Get list of options.
    Options are tuples of (id, display name)
    :return: option list
    """
    cursor = db.get_cursor()
    cursor.execute(SELECT_OPTIONS)
    options = cursor.fetchall()
    options = list(options)
    return options


def get_random_item():
    cursor = db.get_cursor()
    cursor.execute(SELECT_RANDOM_ITEM)
    items = cursor.fetchall()
    if len(items) == 0:
        return None
    return items[0]


def get_item(item_id):
    cursor = db.get_cursor()
    cursor.execute(SELECT_ITEM, (item_id,))
    items = cursor.fetchall()
    if len(items) == 0:
        return None
    return items[0]


def vote(item, option):
    cursor = db.get_cursor()
    cursor.execute(VOTE_FOR_ITEM, (item, option, datetime.datetime.now()))
    count = {}
    total_count = 0
    for option_id, option_name in get_options():
        cursor.execute(COUNT_OPTION_VOTE, (item, option_id))
        count[str(option_id)] = cursor.fetchall()[0][0]
        total_count += count[str(option_id)]
    if total_count < 2:
        return
    for key, value in count.iteritems():
        if value >= total_count / 2:
            log.info("Update item " + str(item) + "'s tag to " + key + ".")
            cursor.execute(UPDATE_ITEM, (int(key), item))
            break
