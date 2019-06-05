Rails.application.routes.draw do
  resources :clientes, param: :identificacion 
  post 'clientecreate', to: 'clientes#create'
end
