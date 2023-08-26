Feature: Searching on DuckDuckGo

  Scenario: Searching for a term
    Given I am on the DuckDuckGo homepage
    When I search for the term "Duck"
    Then I see search results related to the search term
