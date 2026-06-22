# analyzes signal traces for edges stability and transitions


class SignalTraceAnalyzer:
    # stores signal trace analyzer settings
    def __init__(self, config=None):
        self.config = config or {}

    # counts transitions in a signal trace
    def count_transitions(self, samples):
        transitions = 0

        for index in range(1, len(samples)):
            if samples[index] != samples[index - 1]:
                transitions += 1

        return transitions

    # finds indexes where signal transitions occur
    def find_transition_indexes(self, samples):
        transition_indexes = []

        for index in range(1, len(samples)):
            if samples[index] != samples[index - 1]:
                transition_indexes.append(index)

        return transition_indexes

    # checks if a signal trace is stable
    def is_stable(self, samples):
        return self.count_transitions(samples) == 0

    # analyzes a signal trace
    def analyze(self, samples):
        return {
            "analysis": "signal_trace",
            "sample_count": len(samples),
            "transition_count": self.count_transitions(samples),
            "transition_indexes": self.find_transition_indexes(samples),
            "stable": self.is_stable(samples),
        }