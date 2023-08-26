Feature: Searching on DuckDuckGo

  Scenario Outline: Searching for terms from file
    Given I am on the DuckDuckGo homepage
    When I search for the term "<SearchTerm>"
    Then I see search results related to the term "<SearchTerm>"

    Examples:
      | SearchTerm |
      | Duck       |
      | Python     |
      | Behave     |

  Then I capture a screenshot
