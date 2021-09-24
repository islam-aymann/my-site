import {useEffect, useState} from "react";

const data = [
  {
    name: 'Desk and Office',
    description: 'Work from home accessories',
    imageSrc: 'https://tailwindui.com/img/ecommerce-images/home-page-02-edition-01.jpg',
    imageAlt: 'Desk with leather desk pad, walnut desk organizer, wireless keyboard and mouse, and porcelain mug.',
    href: '#',
  },
  {
    name: 'Self-Improvement',
    description: 'Journals and note-taking',
    imageSrc: 'https://tailwindui.com/img/ecommerce-images/home-page-02-edition-02.jpg',
    imageAlt: 'Wood table with porcelain mug, leather journal, brass pen, leather key ring, and a houseplant.',
    href: '#',
  },
  {
    name: 'Travel',
    description: 'Daily commute essentials',
    imageSrc: 'https://tailwindui.com/img/ecommerce-images/home-page-02-edition-03.jpg',
    imageAlt: 'Collection of four insulated travel bottles on wooden shelf.',
    href: '#',
  },
]

export default function Projects() {
const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [hasError, setHasError] = useState(false);

  useEffect(() => {
    setLoading(true);

    fetch("http://127.0.0.1:8000/api/v1/projects/")
      .then((response) => {
        setHasError(!response.ok);
        return response.json();

      })
      .then((json_response) => {
        if (!(200 <= json_response.status && json_response.status <= 300)) {
          setError(json_response);
        }

        setData(json_response)
        setLoading(false);

      })
      .catch((error) => {
        // setError(JSON.stringify(error));
        setLoading(false);
      });


  }, []);

  if (loading) return <h1>Loading...</h1>

  if (hasError) return <pre>Error: {JSON.stringify(error, null, 2)}</pre>;

  if (!data) return <h1>No data</h1>;

  return (
    <div className="bg-gray-100">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="max-w-2xl mx-auto py-16 sm:py-24 lg:py-32 lg:max-w-none">
          <h2 className="text-2xl font-extrabold text-gray-900">Collections</h2>

          <div
            className="mt-6 space-y-12 lg:space-y-0 lg:grid lg:grid-cols-3 lg:gap-x-6">
            {data.map((project) => (
              <div key={project.id} className="group relative">
                <div
                  className="relative w-full h-80 bg-white rounded-lg overflow-hidden group-hover:opacity-75 sm:aspect-w-2 sm:aspect-h-1 sm:h-64 lg:aspect-w-1 lg:aspect-h-1">
                  <img
                    src={project.image}
                    alt={project.imageAlt}
                    className="w-full h-full object-center object-cover"
                  />
                </div>
                <h3 className="mt-6 text-sm text-gray-500">
                  <a href={project.href}>
                    <span className="absolute inset-0"/>
                    {project.title}
                  </a>
                </h3>
                <p
                  className="text-base font-semibold text-gray-900">{project.summary}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}