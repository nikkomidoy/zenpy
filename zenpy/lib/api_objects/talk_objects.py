from zenpy.lib.api_objects import BaseObject
import dateutil.parser


class AccountOverview(BaseObject):
    """
    ######################################################################
    #    Do not modify, this class is autogenerated by gen_classes.py    #
    ######################################################################
    """
    def __init__(self,
                 api=None,
                 average_call_duration=None,
                 average_callback_wait_time=None,
                 average_hold_time=None,
                 average_queue_wait_time=None,
                 average_time_to_answer=None,
                 average_wrap_up_time=None,
                 max_calls_waiting=None,
                 max_queue_wait_time=None,
                 total_call_duration=None,
                 total_callback_calls=None,
                 total_calls=None,
                 total_calls_abandoned_in_queue=None,
                 total_calls_outside_business_hours=None,
                 total_calls_with_exceeded_queue_wait_time=None,
                 total_calls_with_requested_voicemail=None,
                 total_embeddable_callback_calls=None,
                 total_hold_time=None,
                 total_inbound_calls=None,
                 total_outbound_calls=None,
                 total_textback_requests=None,
                 total_voicemails=None,
                 total_wrap_up_time=None,
                 **kwargs):

        self.api = api
        self.average_call_duration = average_call_duration
        self.average_callback_wait_time = average_callback_wait_time
        self.average_hold_time = average_hold_time
        self.average_queue_wait_time = average_queue_wait_time
        self.average_time_to_answer = average_time_to_answer
        self.average_wrap_up_time = average_wrap_up_time
        self.max_calls_waiting = max_calls_waiting
        self.max_queue_wait_time = max_queue_wait_time
        self.total_call_duration = total_call_duration
        self.total_callback_calls = total_callback_calls
        self.total_calls = total_calls
        self.total_calls_abandoned_in_queue = total_calls_abandoned_in_queue
        self.total_calls_outside_business_hours = total_calls_outside_business_hours
        self.total_calls_with_exceeded_queue_wait_time = total_calls_with_exceeded_queue_wait_time
        self.total_calls_with_requested_voicemail = total_calls_with_requested_voicemail
        self.total_embeddable_callback_calls = total_embeddable_callback_calls
        self.total_hold_time = total_hold_time
        self.total_inbound_calls = total_inbound_calls
        self.total_outbound_calls = total_outbound_calls
        self.total_textback_requests = total_textback_requests
        self.total_voicemails = total_voicemails
        self.total_wrap_up_time = total_wrap_up_time

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue


class AgentsActivity(BaseObject):
    """
    ######################################################################
    #    Do not modify, this class is autogenerated by gen_classes.py    #
    ######################################################################
    """
    def __init__(self,
                 api=None,
                 accepted_transfers=None,
                 agent_id=None,
                 available_time=None,
                 avatar_url=None,
                 average_hold_time=None,
                 average_talk_time=None,
                 average_wrap_up_time=None,
                 calls_accepted=None,
                 calls_denied=None,
                 calls_missed=None,
                 calls_put_on_hold=None,
                 forwarding_number=None,
                 name=None,
                 online_time=None,
                 started_transfers=None,
                 status=None,
                 status_code=None,
                 total_call_duration=None,
                 total_hold_time=None,
                 total_talk_time=None,
                 total_wrap_up_time=None,
                 via=None,
                 **kwargs):

        self.api = api
        self.accepted_transfers = accepted_transfers
        self.agent_id = agent_id
        self.available_time = available_time
        self.avatar_url = avatar_url
        self.average_hold_time = average_hold_time
        self.average_talk_time = average_talk_time
        self.average_wrap_up_time = average_wrap_up_time
        self.calls_accepted = calls_accepted
        self.calls_denied = calls_denied
        self.calls_missed = calls_missed
        self.calls_put_on_hold = calls_put_on_hold
        self.forwarding_number = forwarding_number
        self.name = name
        self.online_time = online_time
        self.started_transfers = started_transfers
        self.status = status
        self.status_code = status_code
        self.total_call_duration = total_call_duration
        self.total_hold_time = total_hold_time
        self.total_talk_time = total_talk_time
        self.total_wrap_up_time = total_wrap_up_time
        self.via = via

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue

    @property
    def agent(self):

        if self.api and self.agent_id:
            return self.api._get_agent(self.agent_id)

    @agent.setter
    def agent(self, agent):
        if agent:
            self.agent_id = agent.id
            self._agent = agent


class AgentsOverview(BaseObject):
    """
    ######################################################################
    #    Do not modify, this class is autogenerated by gen_classes.py    #
    ######################################################################
    """
    def __init__(self,
                 api=None,
                 average_accepted_transfers=None,
                 average_available_time=None,
                 average_calls_accepted=None,
                 average_calls_denied=None,
                 average_calls_missed=None,
                 average_calls_put_on_hold=None,
                 average_hold_time=None,
                 average_online_time=None,
                 average_started_transfers=None,
                 average_talk_time=None,
                 average_wrap_up_time=None,
                 total_accepted_transfers=None,
                 total_calls_accepted=None,
                 total_calls_denied=None,
                 total_calls_missed=None,
                 total_calls_put_on_hold=None,
                 total_hold_time=None,
                 total_started_transfers=None,
                 total_talk_time=None,
                 total_wrap_up_time=None,
                 **kwargs):

        self.api = api
        self.average_accepted_transfers = average_accepted_transfers
        self.average_available_time = average_available_time
        self.average_calls_accepted = average_calls_accepted
        self.average_calls_denied = average_calls_denied
        self.average_calls_missed = average_calls_missed
        self.average_calls_put_on_hold = average_calls_put_on_hold
        self.average_hold_time = average_hold_time
        self.average_online_time = average_online_time
        self.average_started_transfers = average_started_transfers
        self.average_talk_time = average_talk_time
        self.average_wrap_up_time = average_wrap_up_time
        self.total_accepted_transfers = total_accepted_transfers
        self.total_calls_accepted = total_calls_accepted
        self.total_calls_denied = total_calls_denied
        self.total_calls_missed = total_calls_missed
        self.total_calls_put_on_hold = total_calls_put_on_hold
        self.total_hold_time = total_hold_time
        self.total_started_transfers = total_started_transfers
        self.total_talk_time = total_talk_time
        self.total_wrap_up_time = total_wrap_up_time

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue


class CurrentQueueActivity(BaseObject):
    """
    ######################################################################
    #    Do not modify, this class is autogenerated by gen_classes.py    #
    ######################################################################
    """
    def __init__(self,
                 api=None,
                 agents_online=None,
                 average_wait_time=None,
                 callbacks_waiting=None,
                 calls_waiting=None,
                 embeddable_callbacks_waiting=None,
                 longest_wait_time=None,
                 **kwargs):

        self.api = api
        self.agents_online = agents_online
        self.average_wait_time = average_wait_time
        self.callbacks_waiting = callbacks_waiting
        self.calls_waiting = calls_waiting
        self.embeddable_callbacks_waiting = embeddable_callbacks_waiting
        self.longest_wait_time = longest_wait_time

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue


class PhoneNumbers(BaseObject):
    """
    ######################################################################
    #    Do not modify, this class is autogenerated by gen_classes.py    #
    ######################################################################
    """
    def __init__(self,
                 api=None,
                 capabilities=None,
                 country_code=None,
                 created_at=None,
                 default_greeting_ids=None,
                 default_group_id=None,
                 display_number=None,
                 greeting_ids=None,
                 group_ids=None,
                 id=None,
                 location=None,
                 name=None,
                 nickname=None,
                 number=None,
                 recorded=None,
                 sms_group_id=None,
                 toll_free=None,
                 transcription=None,
                 **kwargs):

        self.api = api
        self.capabilities = capabilities
        self.country_code = country_code
        self.created_at = created_at
        self.default_greeting_ids = default_greeting_ids
        self.default_group_id = default_group_id
        self.display_number = display_number
        self.greeting_ids = greeting_ids
        self.group_ids = group_ids
        self.id = id
        self.location = location
        self.name = name
        self.nickname = nickname
        self.number = number
        self.recorded = recorded
        self.sms_group_id = sms_group_id
        self.toll_free = toll_free
        self.transcription = transcription

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue

    @property
    def created(self):

        if self.created_at:
            return dateutil.parser.parse(self.created_at)

    @created.setter
    def created(self, created):
        if created:
            self.created_at = created

    @property
    def default_greetings(self):

        if self.api and self.default_greeting_ids:
            return self.api._get_default_greetings(self.default_greeting_ids)

    @default_greetings.setter
    def default_greetings(self, default_greetings):
        if default_greetings:
            self.default_greeting_ids = [o.id for o in default_greetings]
            self._default_greetings = default_greetings

    @property
    def default_group(self):

        if self.api and self.default_group_id:
            return self.api._get_default_group(self.default_group_id)

    @default_group.setter
    def default_group(self, default_group):
        if default_group:
            self.default_group_id = default_group.id
            self._default_group = default_group

    @property
    def greetings(self):

        if self.api and self.greeting_ids:
            return self.api._get_greetings(self.greeting_ids)

    @greetings.setter
    def greetings(self, greetings):
        if greetings:
            self.greeting_ids = [o.id for o in greetings]
            self._greetings = greetings

    @property
    def groups(self):

        if self.api and self.group_ids:
            return self.api._get_groups(self.group_ids)

    @groups.setter
    def groups(self, groups):
        if groups:
            self.group_ids = [o.id for o in groups]
            self._groups = groups

    @property
    def sms_group(self):

        if self.api and self.sms_group_id:
            return self.api._get_sms_group(self.sms_group_id)

    @sms_group.setter
    def sms_group(self, sms_group):
        if sms_group:
            self.sms_group_id = sms_group.id
            self._sms_group = sms_group


class ShowAvailability(BaseObject):
    """
    ######################################################################
    #    Do not modify, this class is autogenerated by gen_classes.py    #
    ######################################################################
    """
    def __init__(self,
                 api=None,
                 available=None,
                 behaviour=None,
                 state_id=None,
                 status=None,
                 via=None,
                 **kwargs):

        self.api = api
        self.available = available
        self.behaviour = behaviour
        self.state_id = state_id
        self.status = status
        self.via = via

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue

    @property
    def state(self):

        if self.api and self.state_id:
            return self.api._get_state(self.state_id)

    @state.setter
    def state(self, state):
        if state:
            self.state_id = state.id
            self._state = state
