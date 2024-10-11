import { ImageResponse } from 'next/og'

// Image metadata
export const size = {
  width: 32,
  height: 32
}

export const contentType = 'image/png'

// Image generation
export default function Icon() {
  return new ImageResponse(
    (
      <div
        style={{
          background: 'linear-gradient(45deg, #336DFF, #1E4FCC)',
          width: '100%',
          height: '100%',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          borderRadius: '8px',
          overflow: 'hidden',
        }}
      >
        {/* For favicon generation, we use regular img tag as ImageResponse 
            doesn't support Next.js Image component */}
        <div
          style={{
            width: '20px',
            height: '20px',
            border: '2.5px solid white',
            borderRadius: '6px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
          }}
        >
          <span style={{ 
            color: 'white', 
            fontSize: '14px',
            fontWeight: 'bold',
            fontFamily: 'SF Pro Display, system-ui, sans-serif',
          }}>
            S
          </span>
        </div>
      </div>
    ),
    {
      ...size,
    }
  )
}