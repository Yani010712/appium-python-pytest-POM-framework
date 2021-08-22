from views.details_view import DetailsView

def test_case_3_details_view_for_the_ship_norwegian_gem_opens(home):
    details = home.nav_to_details_page()

    details.display_element_image(DetailsView.GEM_IMAGE)
    assert details.display_element_text(DetailsView.FACTS_LABEL) == "Ship Facts"
    

def test_Case_4_Verify_ship_details_page_information_for_norwegian_gem(home):
    details = home.nav_to_details_page()
    
    assert details.display_first_element_text(DetailsView.FACTS_LABEL) == "Ship Facts"
    assert details.display_element_text(DetailsView.CREW_LABEL) == "Crew"
    assert details.display_element_text(DetailsView.CREW_VALUE) == "1,070"
    assert details.display_element_text(DetailsView.CRUICE_SPEED) == "Cruise Speed"
    assert details.display_element_text(DetailsView.SPEED_VALUE) == "24 knots"
    assert details.display_element_text(DetailsView.DRAFT_LABEL) == "Draft"
    assert details.display_element_text(DetailsView.DRAFT_VALUE) == "28.2 feet"
    assert details.display_element_text(DetailsView.ENGINES_LABEL) == "Engines"
    assert details.display_element_text(DetailsView.DIESEL_ELECTRIC_LABEL) == "Diesel Electric"
    assert details.display_element_text(DetailsView.GROSS_REGISTER_TONNAGE_LABEL) == "Gross Register Tonnage"
    assert details.display_element_text(DetailsView.GROSS_REGISTER_TONNAGE_VALUE) == "93,530"
    assert details.display_element_text(DetailsView.INAUGURAL_DATE_LABEL) == "Inaugural Date"
    assert details.display_element_text(DetailsView.INAUGURAL_DATE_VALUE) == "2007"
    assert details.display_element_text(DetailsView.MAX_BEAN_LABEL) == "Max Beam"
    assert details.display_element_text(DetailsView.MAX_BEAN_VALUE) == "125 feet"

    home = details.nav_back()


   
    
    

   




  