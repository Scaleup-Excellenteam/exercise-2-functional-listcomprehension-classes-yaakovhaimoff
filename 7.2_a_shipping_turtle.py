"""
Yaakov Haimoff
"""

class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, title, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param str title: The title of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'title': title,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, num_messages=None):
        """Reads messages from a user's inbox.

        :param str username: The username of the inbox to read.
        :param int num_messages: The number of messages to read.
                                If None, read all messages.
        :return: A list of the requested messages.
        :rtype: list
        """
        user_box = self.boxes[username]
        messages_to_read = user_box[:num_messages] if num_messages else user_box
        for message in messages_to_read:
            message['read'] = True
        return messages_to_read

    def search_inbox(self, username, search_term):
        """Searches for messages containing a search term in the title or body.

        :param str username: The username of the inbox to search.
        :param str search_term: The term to search for.
        :return: A list of messages containing the search term.
        :rtype: list
        """
        user_box = self.boxes[username]
        search_results = []
        for message in user_box:
            if search_term in message['body'] or search_term in message['title']:
                search_results.append(message)
        return search_results
