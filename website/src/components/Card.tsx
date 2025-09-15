import { ReactNode } from "react";

export default function Card({title, children}: {title: string, children: ReactNode}): ReactNode {
  return (
    <div className="p-6 bg-[color:var(--chestnut-dark)] rounded-2xl border-2 border-[color:var(--chestnut)]">
      <h2>{title}</h2>
      {children}
    </div>
  )
}