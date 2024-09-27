class Case:
    def __init__(self, case_id, details, status):
        self.case_id = case_id
        self.details = details
        self.status = status
        self.assigned_officers = []

    def assign_officer(self, officer_name):
        self.assigned_officers.append(officer_name)

    def update_case(self, details=None, status=None):
        if details:
            self.details = details
        if status:
            self.status = status

    def _repr_(self):
        return f"Case({self.case_id}, {self.details}, {self.status}, Officers: {self.assigned_officers})"


class CaseManager:
    def __init__(self):
        self.cases = {}

    def add_case(self, case):
        self.cases[case.case_id] = case

    def get_case(self, case_id):
        return self.cases.get(case_id, None)

    def update_case(self, case_id, details=None, status=None):
        case = self.get_case(case_id)
        if case:
            case.update_case(details, status)
        else:
            raise ValueError("Case not found")

    def delete_case(self, case_id):
        if case_id in self.cases:
            del self.cases[case_id]
        else:
            raise ValueError("Case not found")

    def get_all_cases(self):
        return self.cases


class CaseProgress:
    def __init__(self, progress_id, case_id, descriptions):
        self.progress_id = progress_id
        self.case_id = case_id
        self.descriptions = descriptions

    def __repr__(self):
        return f"Progress({self.progress_id}, {self.case_id}, {self.descriptions})"


class CaseProgressTracker:
    def __init__(self):
        self.progress_records = {}

    def add_progress(self, progress):
        self.progress_records[progress.progress_id] = progress

    def view_progress(self, progress_id):
        return self.progress_records.get(progress_id, None)

    def get_all_progress(self):
        return self.progress_records


# Unit Testing the System

import unittest

class TestCaseManagementSystem(unittest.TestCase):
    def setUp(self):
        self.manager = CaseManager()
        self.tracker = CaseProgressTracker()
        self.case1 = Case(case_id="C001", details="Robbery in downtown", status="Open")
        self.progress1 = CaseProgress(progress_id="P001", case_id="C001", descriptions="Initial report filed")

    def test_case_addition(self):
        self.manager.add_case(self.case1)
        self.assertEqual(len(self.manager.get_all_cases()), 1)

    def test_case_update(self):
        self.manager.add_case(self.case1)
        self.manager.update_case("C001", details="Updated details", status="Investigating")
        case = self.manager.get_all_cases()["C001"]
        self.assertEqual(case.details, "Updated details")
        self.assertEqual(case.status, "Investigating")

    def test_case_deletion(self):
        self.manager.add_case(self.case1)
        self.manager.delete_case("C001")
        self.assertEqual(len(self.manager.get_all_cases()), 0)

    def test_progress_tracking(self):
        self.tracker.add_progress(self.progress1)
        progress = self.tracker.view_progress("P001")
        self.assertEqual(progress.descriptions, "Initial report filed")


if __name__ == "__main__":
    unittest.main()
