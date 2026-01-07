# Performance Optimization Strategies

## Algorithm Optimization

### Time Complexity Improvements
```javascript
// O(n²) - Inefficient
function findDuplicates(arr) {
    const duplicates = [];
    for (let i = 0; i < arr.length; i++) {
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[i] === arr[j]) {
                duplicates.push(arr[i]);
            }
        }
    }
    return duplicates;
}

// O(n) - Optimized using Set
function findDuplicates(arr) {
    const seen = new Set();
    const duplicates = new Set();
    for (const item of arr) {
        if (seen.has(item)) {
            duplicates.add(item);
        } else {
            seen.add(item);
        }
    }
    return Array.from(duplicates);
}
```

### Space Complexity Optimization
```javascript
// High memory usage
function processData(data) {
    const results = [];
    for (let i = 0; i < data.length; i++) {
        results.push(expensiveOperation(data[i]));
    }
    return results;
}

// Memory efficient using generator
function* processData(data) {
    for (let i = 0; i < data.length; i++) {
        yield expensiveOperation(data[i]);
    }
}
```

## Data Structure Optimization

### Appropriate Data Structure Selection
```javascript
// Array for lookups - O(n)
const items = ['apple', 'banana', 'cherry'];
const hasItem = items.includes('banana'); // O(n)

// Set for lookups - O(1)
const itemSet = new Set(['apple', 'banana', 'cherry']);
const hasItem = itemSet.has('banana'); // O(1)

// Object vs Map for key-value operations
const obj = { key: 'value' };
const map = new Map([['key', 'value']]);

// Map is better for dynamic keys and better performance
```

### Caching Strategies
```javascript
// Memoization for expensive calculations
const memoize = (fn) => {
    const cache = new Map();
    return (...args) => {
        const key = JSON.stringify(args);
        if (cache.has(key)) {
            return cache.get(key);
        }
        const result = fn(...args);
        cache.set(key, result);
        return result;
    };
};

const expensiveCalculation = memoize((n) => {
    // Expensive calculation
    return n * n;
});
```

## Memory Management

### Memory Leak Prevention
```javascript
// Avoid memory leaks
class EventManager {
    constructor() {
        this.handlers = new Map();
    }

    addEventListener(element, event, handler) {
        element.addEventListener(event, handler);
        this.handlers.set(element, { event, handler });
    }

    removeEventListener(element) {
        const entry = this.handlers.get(element);
        if (entry) {
            element.removeEventListener(entry.event, entry.handler);
            this.handlers.delete(element);
        }
    }

    cleanup() {
        for (const [element, entry] of this.handlers) {
            element.removeEventListener(entry.event, entry.handler);
        }
        this.handlers.clear();
    }
}
```

### Efficient DOM Manipulation
```javascript
// Inefficient - multiple DOM updates
function updateList(items) {
    const container = document.getElementById('list');
    container.innerHTML = '';
    items.forEach(item => {
        const div = document.createElement('div');
        div.textContent = item;
        container.appendChild(div);
    });
}

// Efficient - single DOM update
function updateList(items) {
    const container = document.getElementById('list');
    const fragment = document.createDocumentFragment();
    items.forEach(item => {
        const div = document.createElement('div');
        div.textContent = item;
        fragment.appendChild(div);
    });
    container.innerHTML = '';
    container.appendChild(fragment);
}
```

## Network Optimization

### Request Optimization
```javascript
// Batch requests
const batchRequests = async (requests) => {
    const responses = await Promise.all(
        requests.map(req => fetch(req.url))
    );
    return responses;
};

// Lazy loading
const lazyLoadImages = () => {
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                imageObserver.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));
};
```

### Data Compression
```javascript
// Compress data before sending
const compressData = (data) => {
    return JSON.stringify(data);
};

// Use gzip compression on server
// Configure server to compress responses
```

## Code Splitting and Lazy Loading

### Dynamic Imports
```javascript
// Lazy load heavy modules
const loadHeavyModule = async () => {
    const { heavyFunction } = await import('./heavy-module');
    return heavyFunction();
};

// Route-based code splitting
const routes = {
    '/home': () => import('./pages/Home'),
    '/about': () => import('./pages/About'),
    '/dashboard': () => import('./pages/Dashboard')
};
```

### Component Lazy Loading
```javascript
// React example
import { lazy, Suspense } from 'react';

const LazyComponent = lazy(() => import('./HeavyComponent'));

function App() {
    return (
        <Suspense fallback={<div>Loading...</div>}>
            <LazyComponent />
        </Suspense>
    );
}
```

## Browser-Specific Optimizations

### RequestAnimationFrame
```javascript
// Smooth animations
let animationId;
let lastTime = 0;

function animate(currentTime) {
    if (lastTime === 0) lastTime = currentTime;

    const deltaTime = currentTime - lastTime;
    lastTime = currentTime;

    // Update logic here
    update(deltaTime);

    animationId = requestAnimationFrame(animate);
}

// Start animation
animationId = requestAnimationFrame(animate);

// Stop animation
cancelAnimationFrame(animationId);
```

### Web Workers
```javascript
// Offload heavy computation
const worker = new Worker('worker.js');

worker.postMessage({ data: largeDataSet });
worker.onmessage = (event) => {
    const result = event.data;
    // Handle result
};

// worker.js
self.onmessage = function(event) {
    const data = event.data.data;
    const result = heavyComputation(data);
    self.postMessage(result);
};
```

## Performance Monitoring

### Performance Measurement
```javascript
// Measure function execution time
const measurePerformance = (fn, name) => {
    const start = performance.now();
    const result = fn();
    const end = performance.now();
    console.log(`${name}: ${end - start}ms`);
    return result;
};

// Measure memory usage
const measureMemory = () => {
    if (performance.memory) {
        console.log('Memory usage:', {
            used: Math.round(performance.memory.usedJSHeapSize / 1048576) + 'MB',
            total: Math.round(performance.memory.totalJSHeapSize / 1048576) + 'MB',
            limit: Math.round(performance.memory.jsHeapSizeLimit / 1048576) + 'MB'
        });
    }
};
```

### Profiling Tools
```javascript
// Chrome DevTools performance profiling
// Use Performance tab to record and analyze
// Look for:
// - Long tasks (>50ms)
// - Main thread blocking
// - Memory leaks
// - Expensive operations

// Lighthouse for web performance
// Run audits for:
// - Performance score
// - Best practices
// - Accessibility
// - SEO
```

## Best Practices Summary

### Development Phase
- Profile before optimizing
- Use appropriate data structures
- Implement caching strategies
- Optimize algorithms and complexity

### Build Phase
- Enable tree shaking
- Use code splitting
- Minify and compress assets
- Optimize images

### Runtime Phase
- Monitor performance metrics
- Implement error boundaries
- Use progressive loading
- Optimize for mobile devices

### Continuous Monitoring
- Set up performance budgets
- Monitor Core Web Vitals
- Track user experience metrics
- Regular performance audits