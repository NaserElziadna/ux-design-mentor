# Mobile-First Design

**Primary Goals:**
- Fast, responsive experience
- Touch-friendly interaction
- Offline capability
- Battery/data efficiency

**Core Principles (Adapted):**
1. **Touch-first** (Don Norman - affordances)
   - 44px minimum touch targets
   - Spacing between targets
   - Visual feedback on touch
   - Forgiving targets
   - Avoid hover-dependent

2. **Performance** (Krug - simplicity = speed)
   - <3 second load time
   - Optimize images
   - Minimize requests
   - Lazy load
   - Progressive enhancement

3. **Responsive design** (Tidwell - patterns)
   - Works on all screen sizes
   - Adapts to portrait/landscape
   - Readable text (16px minimum)
   - Scrollable not scrolling
   - Single column optimal

4. **Progressive disclosure** (Krug, Norman)
   - Hide less critical options
   - Show relevant content first
   - Drill-down for details
   - Minimize scrolling
   - Bottom navigation for primary

5. **Offline capability** (Brown)
   - Works without connection
   - Sync when available
   - Clear offline indicators
   - Local caching
   - Graceful degradation

**Critical Metrics:**
- Load time (mobile)
- Bounce rate
- Conversion rate
- Device compatibility
- Battery impact

**Common Mobile Patterns:**
- Bottom navigation (primary actions)
- Hamburger menu (secondary)
- Tab bar navigation
- Cards (scrollable)
- Swipe interactions
- Gesture-based

**Critical Mistakes to Avoid:**
- ❌ Designing for desktop first
- ❌ Tiny touch targets (<44px)
- ❌ Slow images / unoptimized
- ❌ Horizontal scrolling
- ❌ Hover-only interactions
- ❌ Too much scrolling needed
- ❌ Unreadable text

**Testing Approach:**
- Test on actual devices
- Mobile speed testing
- User testing with mobile users
- Offline scenario testing
- Touch interaction testing
