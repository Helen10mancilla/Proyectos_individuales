import React, { useState } from "react";

const steps = [
  "Paso 1: Información Personal",
  "Paso 2: Contacto",
  "Paso 3: Confirmación"
];

const FormularioPasoAPaso = () => {
  const [currentStep, setCurrentStep] = useState(0);
  const [formData, setFormData] = useState({
    nombre: "",
    email: "",
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleNextStep = () => {
    if (currentStep < steps.length - 1) {
      setCurrentStep(currentStep + 1);
    }
  };

  const handlePrevStep = () => {
    if (currentStep > 0) {
      setCurrentStep(currentStep - 1);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-black">
      <div className="bg-gray-800 p-8 rounded-lg shadow-lg w-full max-w-md">
        <h2 className="text-2xl text-white mb-4">{steps[currentStep]}</h2>

        {currentStep === 0 && (
          <div className="mb-4">
            <label className="block text-white mb-2">Nombre:</label>
            <input
              type="text"
              name="nombre"
              value={formData.nombre}
              onChange={handleInputChange}
              className="w-full px-4 py-2 text-black rounded"
            />
          </div>
        )}

        {currentStep === 1 && (
          <div className="mb-4">
            <label className="block text-white mb-2">Email:</label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleInputChange}
              className="w-full px-4 py-2 text-black rounded"
            />
          </div>
        )}

        {currentStep === 2 && (
          <div className="text-white">
            <p>¡Formulario completado!</p>
            <p>Nombre: {formData.nombre}</p>
            <p>Email: {formData.email}</p>
          </div>
        )}

        <div className="mt-4 flex justify-between">
          <button
            onClick={handlePrevStep}
            disabled={currentStep === 0}
            className="bg-gray-600 text-white px-4 py-2 rounded"
          >
            Atrás
          </button>

          {currentStep < steps.length - 1 ? (
            <button
              onClick={handleNextStep}
              className="bg-blue-600 text-white px-4 py-2 rounded"
            >
              Siguiente
            </button>
          ) : (
            <button className="bg-green-600 text-white px-4 py-2 rounded">
              Enviar
            </button>
          )}
        </div>
      </div>
    </div>
  );
};

export default FormularioPasoAPaso;
