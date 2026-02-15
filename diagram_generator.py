from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Client
from diagrams.programming.language import Python
from diagrams.custom import Custom
from diagrams.saas.chat import Slack  # Representing CrewAI Agents generically

with Diagram("MarketMindAI Architecture", show=False, direction="LR"):
    user = Client("User")

    with Cluster("MarketMindAI Crew"):
        crew_engine = Python("CrewAI Engine")
        
        with Cluster("Agents"):
            market_researcher = Slack("Market Research\nSpecialist")
            competitor_analyst = Slack("Competitive\nIntelligence Analyst")
            customer_researcher = Slack("Customer Insights\nResearcher")
            product_strategist = Slack("Product Strategy\nAdvisor")
            business_analyst = Slack("Business Analyst")

        with Cluster("Tools"):
            try:
                from diagrams.aws.general import InternetAlt2
                serper = InternetAlt2("Serper Dev Tool")
                scraper = InternetAlt2("Scrape Website Tool")
            except ImportError:
                 # Fallback to generic nodes if specific icons not available
                 serper = Client("Serper Dev Tool")
                 scraper = Client("Scrape Website Tool")

    user >> Edge(label="Input: Product Idea") >> crew_engine
    
    crew_engine >> market_researcher
    market_researcher >> competitor_analyst
    competitor_analyst >> customer_researcher
    customer_researcher >> product_strategist
    product_strategist >> business_analyst
    
    business_analyst >> Edge(label="Output: Report.md") >> user

    # Tool usage
    agents = [market_researcher, competitor_analyst, customer_researcher, product_strategist, business_analyst]
    for agent in agents:
        agent >> Edge(style="dotted") >> serper
        agent >> Edge(style="dotted") >> scraper
