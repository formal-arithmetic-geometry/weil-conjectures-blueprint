+++
id = "pur713-def-mapmod"
kind = "definition"
title = "Transport of module objects"
order = 2344
+++
Let $F:\mathscr C\to\mathscr D$ be a lax symmetric monoidal functor between symmetric monoidal categories, with lax structure maps $m_{A,B}:FA\otimes FB\to F(A\otimes B)$ and $m_0:\mathbb 1\to F\mathbb 1$, and let $\mathcal R$ be a commutative ring object in $\mathscr C$ with multiplication $\mu$ and unit $e$. Then $F\mathcal R$, with multiplication $F(\mu)\circ m_{\mathcal R,\mathcal R}$ and unit $F(e)\circ m_0$, is a commutative ring object of $\mathscr D$: its associativity, unit and commutativity equations follow from those of $\mathcal R$ and the coherence equations of the lax symmetric monoidal structure. Applying $F$ to module objects gives a functor
$F_{\mathcal R}:\mathsf{Mod}_{\mathcal R}(\mathscr C)\to\mathsf{Mod}_{F\mathcal R}(\mathscr D)$.
It sends a module $M$ to $FM$, with action the composite
$F\mathcal R\otimes FM\xrightarrow{m_{\mathcal R,M}}F(\mathcal R\otimes M)\to FM$,
and sends morphisms by $F$. In the applications below $\mathscr C,\mathscr D$ are categories of abelian sheaves on pro-étale sites with $\otimes_{\mathbf Z}$, and $F$ is $u_{*,\mathbf Z}$ or $u^{-1}_{\mathbf Z}$ with the structures of Input “Monoidality of fixed-coefficient images” (`pur713-input-fixed-monoidal`). This is the functor $\mathrm{mapMod}(F)$ of the governing reference.
