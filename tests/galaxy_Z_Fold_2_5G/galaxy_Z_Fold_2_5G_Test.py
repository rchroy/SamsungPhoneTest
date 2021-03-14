from pages.galaxy_Z_Fold_2_5G.galaxy_Z_Fold_2_5G_Page import galaxy_z_fold2_5g
import pytest
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class galaxy_Z_Fold_2_5G_Tests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.brp = galaxy_z_fold2_5g(self.driver)

    @pytest.mark.run
    def test_browsing(self):
        self.brp.galaxy_z_fold2_5g_browsing()

