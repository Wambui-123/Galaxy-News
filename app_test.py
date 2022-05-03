import unittest

# class news_source(unittest.TestCase):
#     def setUp(self):
#         self.app = create_app()
#         self.app.config['WTF_CSRF_ENABLED'] = False  # no CSRF during tests
#         self.appctx = self.app.app_context()
#         self.appctx.push()
#         db.create_all()
#         self.populate_db()
#         self.client = self.app.test_client()