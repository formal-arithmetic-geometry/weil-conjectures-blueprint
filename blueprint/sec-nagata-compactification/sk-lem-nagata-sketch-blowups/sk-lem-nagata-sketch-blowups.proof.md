+++
kind  = "proof"
of    = "sk-lem-nagata-sketch-blowups"
uses = ["sk-lem-nagata-sketch-closure", "sk-def-nagata-admissible"]
+++
For ideals $\mathcal I,\mathcal J$, blowing up their product factors through
both blow-ups. Indeed, after the product becomes an invertible ideal, each
factor is invertible, and the universal property applies. More explicitly,
first blowing up $\mathcal I$ and then the pulled-back $\mathcal J$ gives the
blow-up of $\mathcal I\mathcal J$ (Stacks 080A). Induction proves the first
assertion. For a center on the first blow-up which is not itself pulled back
from $T$, the composition assertion is the finite-type ideal calculation in
Stacks 080B.

The extension assertion uses extension of finite-type quasi-coherent ideals
from a quasi-compact open, with a center still outside $U$; the precise
admissible extension result is Stacks 080M. These two results turn finitely
many local constructions into one global modification preserving $U$.
