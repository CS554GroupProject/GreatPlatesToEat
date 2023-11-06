import { render, screen } from '@testing-library/react';
import App from './App';

test('renders the default page text', () => {
  render(<App />);
  const linkElement = screen.getByText(/This is the default page or path/i);
  expect(linkElement).toBeInTheDocument();
});
