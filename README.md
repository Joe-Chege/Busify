
# **IoTron-Busify**

IoTron-Busify is a modern IoT-powered system designed for school management, focusing on geospatial tracking of partner schools and vehicles. The system leverages Django, Django REST Framework, MongoEngine, and Leaflet.js to offer real-time data visualization and interaction.

---

## **Features**
### **1. Partner School Management**
- Add and manage school data with geospatial information (coordinates and addresses).
- Dynamically display schools on an interactive map.
- Fetch school details through RESTful APIs.

### **2. Geospatial Mapping**
- View schools and vehicle locations on a live map using **Leaflet.js** with **Mapbox** tiles.
- Highlight school locations with markers and allow dynamic zoom functionality.

### **3. Vehicle Tracking**
- Track real-time vehicle locations (future feature).

### **4. RESTful API**
- Full CRUD operations for managing school data via APIs.
- GeoJSON integration for geospatial data.

---

## **Tech Stack**
- **Backend**:
  - Python 3.10
  - Django 4.x
  - Django REST Framework
  - MongoEngine
- **Database**:
  - MongoDB (Atlas for cloud-hosted database)
- **Frontend**:
  - Leaflet.js
  - Mapbox tiles
- **Geospatial**:
  - GeoJSON for storing location data.

---

## **Installation and Setup**

### **1. Prerequisites**
- Python 3.10+
- MongoDB (Atlas recommended or a local MongoDB instance)
- Node.js and npm (for additional front-end dependencies if needed)

### **2. Clone the Repository**
```bash
git clone https://github.com/your-username/iotron-busify.git
cd iotron-busify
```

### **3. Set Up the Virtual Environment**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### **4. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **5. Configure MongoDB**
- Set up a MongoDB Atlas cluster or use a local instance.
- Update `settings.py` with your MongoDB connection details:
  ```python
  from mongoengine import connect
  connect(
      db='Iotron',
      host='mongodb+srv://your_username:your_password@cluster.mongodb.net/?retryWrites=true&w=majority',
      username='your_username',
      password='your_password',
      authentication_source='admin',
      authentication_mechanism='SCRAM-SHA-1'
  )
  ```

### **6. Run Migrations**
If using `djongo` for MongoDB integration:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## **Usage**

### **1. Start the Development Server**
```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000`.

### **2. API Endpoints**
#### **List Schools**
**GET** `/api/schools/`  
Fetch all partner schools.

#### **Create School**
**POST** `/api/schools/`  
Example payload:
```json
{
    "name": "Dreamers Academy",
    "location": {
        "type": "Point",
        "coordinates": [-1.2811, 36.8064]
    },
    "address": "Nairobi"
}
```

---

## **Map Integration**

The map is powered by **Leaflet.js** with **Mapbox Satellite Streets**. On loading the application:
1. **Initial View**:
   - Displays Nairobi County with partner schools marked on the map.
2. **Dynamic Updates**:
   - Fetches school data from `/api/schools/` and plots them as markers.
3. **Interactive Sidebar**:
   - Click a school name to zoom in on its location.

### **Custom School Icon**
- Marker icons for schools are customizable using the `school-icon.png` located in `/static`.

---

## **File Structure**

```
iotron-busify/
├── GeoTracker/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── tracker/
│   ├── models.py        # School and vehicle models
│   ├── serializers.py   # DRF serializers for APIs
│   ├── urls.py          # API routes
│   ├── views.py         # API and view logic
│   ├── static/          # Static assets (icons, CSS, JS)
│   └── templates/       # HTML templates
└── requirements.txt
```



## **Contributing**

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make changes and commit:
   ```bash
   git commit -m "Add your message"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## **Future Enhancements**
- Real-time vehicle tracking.
- Admin dashboard for managing schools and vehicles.
- Geofencing for school buses.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Acknowledgments**
- **Mapbox**: For beautiful tile layers.
- **Leaflet.js**: For interactive mapping.
- **MongoDB**: For scalable database solutions.

---

Let me know if you'd like to add more details or examples! 🚀

