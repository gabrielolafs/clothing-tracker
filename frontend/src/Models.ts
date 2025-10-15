export interface Garment {
    id: number
    type: string
    brand: string | null
    color: string | null
    size: string | null
    price_paid: number | null
    times_worn: number
    times_since_washed: number
    times_needed_before_wash: number
    specific_attributes: Record<string, any> | null
    created_at: string  // ISO date string from API
    last_time_worn: string | null  // ISO date string from API
}