import { ReactNode } from "react";

export default function Orange({children}: {children: string}): ReactNode {
  return <span className="text-orange-300">{children}</span>
}