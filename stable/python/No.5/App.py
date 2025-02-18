import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class ProjectConfig:
    name: str
    description: str
    technologies: List[str]
    icon: str
    color: str

@dataclass
class ServiceConfig:
    name: str
    description: str
    icon: str
    color: str

class PortfolioConfig:
    def __init__(self):
        self.projects = [
            ProjectConfig(
                name="Neural Network Explorer",
                description="Advanced AI-powered data analysis platform",
                technologies=["PyTorch", "React", "Docker"],
                icon="fas fa-brain",
                color="text-red-500"
            ),
            ProjectConfig(
                name="Quantum Visualization",
                description="Real-time quantum computing simulation",
                technologies=["Qiskit", "D3.js", "WebGL"],
                icon="fas fa-atom",
                color="text-blue-500"
            )
        ]

        self.services = [
            ServiceConfig(
                name="Software Engineering",
                description="Cutting-edge solution development",
                icon="fas fa-code",
                color="text-yellow-500"
            ),
            ServiceConfig(
                name="AI Consulting",
                description="Intelligent system design",
                icon="fas fa-robot",
                color="text-red-500"
            ),
            ServiceConfig(
                name="Cloud Architecture",
                description="Scalable infrastructure solutions",
                icon="fas fa-cloud",
                color="text-blue-500"
            )
        ]

class PortfolioApp:
    def __init__(self):
        self.config = PortfolioConfig()
        self.app = dash.Dash(__name__,
            external_stylesheets=[
                "https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"
            ],
            meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}]
        )

        self.app.title = "Quantum Digital Portfolio"
        self.app.layout = self._create_layout()
        self._register_callbacks()

    def _create_layout(self):
        return html.Div([
            # Navigation
            html.Nav([
                html.Div([
                    html.Div([
                        html.Span("AR", className="text-2xl font-bold text-white bg-red-500 px-3 py-1 rounded-full mr-4"),
                        html.Div([
                            html.A("Home", href="/", className="mx-3 text-blue-600 hover:text-yellow-500 transition duration-300"),
                            html.A("Projects", href="/projects", className="mx-3 text-blue-600 hover:text-yellow-500 transition duration-300"),
                            html.A("Services", href="/services", className="mx-3 text-blue-600 hover:text-yellow-500 transition duration-300"),
                            html.A("Contact", href="/contact", className="mx-3 text-blue-600 hover:text-yellow-500 transition duration-300")
                        ], className="inline-block")
                    ], className="flex items-center justify-between")
                ], className="container mx-auto py-6")
            ], className="border-b border-gray-200 shadow-sm"),

            # Dynamic Content
            html.Div(id='page-content', className='min-h-screen'),

            # Footer
            html.Footer([
                html.Div([
                    html.Div([
                        html.Div([
                            html.A(html.I(className="fab fa-github text-2xl mr-4 text-blue-600 hover:text-red-500 transition duration-300"), href="#"),
                            html.A(html.I(className="fab fa-linkedin text-2xl mr-4 text-blue-600 hover:text-yellow-500 transition duration-300"), href="#"),
                            html.A(html.I(className="fab fa-twitter text-2xl text-blue-600 hover:text-red-500 transition duration-300"), href="#")
                        ], className="flex justify-center mb-4")
                    ], className="container mx-auto")
                ], className="bg-gray-100 py-8")
            ]),

            # Routing
            dcc.Location(id='url', refresh=False)
        ])

    def _register_callbacks(self):
        @self.app.callback(
            Output('page-content', 'children'),
            [Input('url', 'pathname')]
        )
        def display_page(pathname):
            page_routes = {
                '/': self.home_page,
                '/projects': self.projects_page,
                '/services': self.services_page,
                '/contact': self.contact_page
            }
            return page_routes.get(pathname, self.home_page)()

    def home_page(self):
        return html.Div([
            html.Div([
                html.Div([
                    html.H1("Alex Rodriguez", className="text-6xl font-bold mb-4 text-blue-600"),
                    html.H2("Quantum Software Architect", className="text-2xl text-red-500 mb-8"),
                    html.P("Bridging the gap between innovative technology and transformative solutions.",
                           className="text-xl text-yellow-500 mb-12"),
                    html.Div([
                        # Advanced Projects Button
                        html.A([
                            html.Div([
                                html.I(className="fas fa-project-diagram mr-3"),
                                "View Projects",
                                html.Span(className="absolute inset-0 bg-blue-500 opacity-0 group-hover:opacity-25 transition-opacity duration-300 rounded-full")
                            ], className="relative px-8 py-3 bg-white text-blue-600 border-2 border-blue-600 rounded-full font-bold transform transition-all duration-300 hover:-translate-y-1 hover:shadow-lg group overflow-hidden")
                        ], href="/projects"),

                        # Advanced CV Download Button
                        html.A([
                            html.Div([
                                html.I(className="fas fa-download mr-3"),
                                "Download CV",
                                html.Span(className="absolute inset-0 bg-yellow-500 opacity-0 group-hover:opacity-25 transition-opacity duration-300 rounded-full")
                            ], className="relative px-8 py-3 bg-white text-yellow-600 border-2 border-yellow-600 rounded-full font-bold transform transition-all duration-300 hover:-translate-y-1 hover:shadow-lg group overflow-hidden ml-4")
                        ], href="#")
                    ], className="flex justify-center space-x-4")
                ], className="text-center max-w-2xl mx-auto")
            ], className="flex items-center justify-center min-h-screen")
        ])

    def projects_page(self):
        return html.Div([
            html.Div([
                html.H2("Featured Projects", className="text-4xl font-bold text-center mb-16 text-blue-600"),
                html.Div([
                    html.Div([
                        html.Div([
                            html.I(className=f"{project.icon} text-5xl mb-6 {project.color}"),
                            html.H3(project.name, className="text-2xl font-bold mb-4 text-red-500"),
                            html.P(project.description, className="text-yellow-500 mb-6"),
                            html.Div([
                                html.Span(tech, className="bg-blue-100 text-blue-600 px-3 py- 1 rounded-full text-sm mr-2 mb-2")
                                for tech in project.technologies
                            ], className="flex flex-wrap"),

                            # Advanced Project Details Button
                            html.Div([
                                html.Button([
                                    "Explore Project ",
                                    html.I(className="fas fa-arrow-right ml-2")
                                ], className="group relative px-6 py-2 bg-red-500 text-white rounded-full overflow-hidden transform transition-all duration-300 hover:pr-8 hover:bg-red-600")
                            ], className="mt-4 flex justify-center")
                        ], className="p-8 border border-gray-200 rounded-lg hover:shadow-lg transition-all")
                    ], className="mb-8") for project in self.config.projects
                ], className="grid md:grid-cols-2 gap-8")
            ], className="container mx-auto py-20")
        ])

    def services_page(self):
        return html.Div([
            html.Div([
                html.H2("Professional Services", className="text-4xl font-bold text-center mb-16 text-blue-600"),
                html.Div([
                    html.Div([
                        html.Div([
                            html.I(className=f"{service.icon} text-5xl mb-6 {service.color}"),
                            html.H3(service.name, className="text-2xl font-bold mb-4 text-red-500"),
                            html.P(service.description, className="text-yellow-500 mb-6"),

                            # Advanced Service Details Button
                            html.Div([
                                html.Button([
                                    "Learn More ",
                                    html.I(className="fas fa-info-circle ml-2")
                                ], className="group relative px-6 py-2 bg-blue-500 text-white rounded-full overflow-hidden transform transition-all duration-300 hover:pr-8 hover:bg-blue-600")
                            ], className="mt-4 flex justify-center")
                        ], className="text-center p-8 border border-gray-200 rounded-lg hover:shadow-lg transition-all")
                    ]) for service in self.config.services
                ], className="grid md:grid-cols-3 gap-8")
            ], className="container mx-auto py-20")
        ])

    def contact_page(self):
        return html.Div([
            html.Div([
                html.H2("Get In Touch", className="text-4xl font-bold text-center mb-16 text-blue-600"),
                html.Div([
                    dcc.Input(id='contact-name', placeholder="Your Name", className="input input-bordered w-full mb-4"),
                    dcc.Input(id='contact-email', placeholder="Your Email", type="email", className="input input-bordered w-full mb-4"),
                    dcc.Textarea(id='contact-message', placeholder="Your Message", className="textarea textarea-bordered w-full mb-4"),

                    # Advanced Send Message Button
                    html.Div([
                        html.Button([
                            html.I(className="fas fa-paper-plane mr-3"),
                            "Send Message",
                            html.Span(className="absolute inset-0 bg-red-500 opacity-0 group-hover:opacity-25 transition-opacity duration-300 rounded-full")
                        ], id='send-button', className="group relative px-8 py-3 bg-white text-red-600 border-2 border-red-600 rounded-full font-bold transform transition-all duration-300 hover:-translate-y-1 hover:shadow-lg overflow-hidden")
                    ], className="flex justify-center")
                ], className="bg-white p-8 border border-gray-200 rounded-lg shadow-lg")
            ], className="container mx-auto py-20")
        ])

    def run(self):
        self.app.run_server(debug=True)

if __name__ == '__main__':
    app = PortfolioApp()
    app.run()
