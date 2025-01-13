export const places = [
  {
    id: 1,
    name: "Beautiful Beach House",
    host: "John Doe",
    price: 150,
    description: "A beautiful beach house with amazing views...",
    amenities: "WiFi, Pool, Air Conditioning",
    reviews: [
      { author: "Jane Smith", comment: "Great place to stay!", rating: 4 },
      { author: "Robert Brown", comment: "Amazing location and very comfortable.", rating: 5 },
    ],
  },
  {
    id: 2,
    name: "Cozy Cabin",
    host: "Alice Johnson",
    price: 100,
    description: "A warm and inviting cabin in the woods.",
    amenities: "Fireplace, Hiking Trails, Mountain View",
    reviews: [
      { author: "Emma Wilson", comment: "So cozy and quiet!", rating: 5 },
    ],
  },
  {
    id: 3,
    name: "Modern Apartment",
    host: "Chris Lee",
    price: 200,
    description: "A sleek and stylish city apartment with modern amenities.",
    amenities: "Smart TV, High-Speed WiFi, Gym Access",
    reviews: [
      { author: "Liam Martinez", comment: "Perfect for business travel.", rating: 4 },
    ],
  },
  {
    id: 4,
    name: "Rustic Lakehouse",
    host: "Laura White",
    price: 180,
    description: "A charming lakehouse with a beautiful view of the sunset.",
    amenities: "Boat Dock, Fireplace, Private Garden",
    reviews: [
      { author: "Michael Scott", comment: "Absolutely stunning and relaxing!", rating: 5 },
      { author: "Pam Beesly", comment: "Perfect place for a getaway.", rating: 4 },
    ],
  },
  {
    id: 5,
    name: "Penthouse Suite",
    host: "David Beckham",
    price: 350,
    description: "A luxurious penthouse with panoramic city views.",
    amenities: "Private Pool, Rooftop Bar, 24/7 Butler Service",
    reviews: [
      { author: "Victoria Beckham", comment: "Luxury at its finest!", rating: 5 },
      { author: "Elton John", comment: "Absolutely worth it!", rating: 5 },
    ],
  },
];



const places = [
  {
    id: "765a38e6-c131-4315-8e9c-28ac88424634",
    name: "Beautiful Beach House",
    host: "John Doe",
    price: 150,
    description: "A beautiful beach house with amazing views...",
    amenities: ["WiFi", "Pool", "Air Conditioning"],
    reviews: [
      { author: "Jane Smith", comment: "Great place to stay!", rating: 4 },
      { author: "Robert Brown", comment: "Amazing location and very comfortable.", rating: 5 },
    ],
  },
  {
    id: "5c66b5f9-74a7-4767-8f5b-7d2b153b6057",
    name: "Cozy Cabin",
    host: "Alice Johnson",
    price: 100,
    description: "A warm and inviting cabin in the woods.",
    amenities: ["Fireplace", "Hiking Trails", "Mountain View"],
    reviews: [
      { author: "Emma Wilson", comment: "So cozy and quiet!", rating: 5 },
    ],
  },
  {
    id: "3f477fd8-fc69-47f1-8c22-12dc4db86099",
    name: "Modern Apartment",
    host: "Chris Lee",
    price: 200,
    description: "A sleek and stylish city apartment with modern amenities.",
    amenities: ["Smart TV", "High-Speed WiFi", "Gym Access"],
    reviews: [
      { author: "Liam Martinez", comment: "Perfect for business travel.", rating: 4 },
    ],
  },
  {
    id: "13e66193-3e0b-493d-bca2-94252343a5e3",
    name: "Rustic Lakehouse",
    host: "Laura White",
    price: 180,
    description: "A charming lakehouse with a beautiful view of the sunset.",
    amenities: ["Boat Dock", "Fireplace", "Private Garden"],
    reviews: [
      { author: "Michael Scott", comment: "Absolutely stunning and relaxing!", rating: 5 },
      { author: "Pam Beesly", comment: "Perfect place for a getaway.", rating: 4 },
    ],
  },
  {
    id: "377822b5-1601-43d9-866d-15db7932579f",
    name: "Penthouse Suite",
    host: "David Beckham",
    price: 350,
    description: "A luxurious penthouse with panoramic city views.",
    amenities: ["Private Pool", "Rooftop Bar", "24/7 Butler Service"],
    reviews: [
      { author: "Victoria Beckham", comment: "Luxury at its finest!", rating: 5 },
      { author: "Elton John", comment: "Absolutely worth it!", rating: 5 },
    ],
  },
  {
    id: "5e5a38e6-c231-4315-8e9c-28ac88425634",
    name: "Super Cheap Room",
    host: "Bob Builder",
    price: 5,
    description:
      "An ultra-affordable room with shared facilities. Great for adventurers on a budget.",
    amenities: ["WiFi", "Free Breakfast"],
    reviews: [
      { author: "Alice Johnson", comment: "I stayed here for 5€, and it was worth all 5 coins.", rating: 4 },
    ],
  },
  {
    id: "6c66b5f9-75b7-4767-8f5b-7d2b153b7057",
    name: "Cheaper Cabin",
    host: "Mickey Mouse",
    price: 10,
    description: "Still cozy but much cheaper than its cousin.",
    amenities: ["Fireplace", "Hiking Trails"],
    reviews: [
      { author: "Emma Wilson", comment: "Amazing place, but bring your own tea.", rating: 5 },
    ],
  },
  {
    id: "4f477fd8-fd69-47f1-8c22-12dc4db86199",
    name: "Nice Apartment",
    host: "Harry Potter",
    price: 49,
    description: "A moderately priced apartment with all essentials.",
    amenities: ["Swimming Pool", "Air Conditioning"],
    reviews: [
      { author: "John Doe", comment: "The host vanished, but the room was great.", rating: 3 },
    ],
  },
  {
    id: "7e66193-4f0b-493d-bca2-94252343b5e3",
    name: "Family Lakehouse",
    host: "Tony Stark",
    price: 50,
    description: "A great lakehouse with space for the entire family.",
    amenities: ["Smart TV", "Pet-Friendly"],
    reviews: [
      { author: "Sherlock Holmes", comment: "Cozy house but haunted vibes.", rating: 4 },
    ],
  },
  {
    id: "9c822b5-2601-43d9-866d-15db7932589f",
    name: "Modern Villa",
    host: "Sherlock Holmes",
    price: 70,
    description: "A stunning villa perfect for a luxury retreat.",
    amenities: ["Smart Home Automation", "High-Speed WiFi"],
    reviews: [
      { author: "Tony Stark", comment: "The villa was so modern, even my cat got Wi-Fi.", rating: 5 },
    ],
  },
  {
    id: "3c88b0a2-b1a9-410e-a18c-4f5cd017ebae",
    name: "Elegant Mansion",
    host: "Bob Builder",
    price: 350,
    description: "An elegant mansion with stunning architecture.",
    amenities: ["Smart TV", "Private Garden"],
    reviews: [
      { author: "Laura White", comment: "This mansion is so elegant, I got inspired to write a novel.", rating: 5 },
    ],
  },
];
