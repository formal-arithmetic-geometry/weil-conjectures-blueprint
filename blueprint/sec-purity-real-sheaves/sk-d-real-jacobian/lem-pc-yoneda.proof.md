+++
kind  = "proof"
of    = "lem-pc-yoneda"
+++
Write $\xi_\tau=\tau_X(\mathrm{id}_X)$. For a scheme $T/S$ and
$f\in h_X(T)=\operatorname{Hom}_S(T,X)$ we have $f=h_X(f)(\mathrm{id}_X)$, so
naturality of $\tau$ gives

$$
\tau_T(f)=\tau_T\bigl(h_X(f)(\mathrm{id}_X)\bigr)=F(f)(\xi_\tau).
$$

Hence $\tau$ is determined by $\xi_\tau$, and the map is injective.
Conversely, for $\xi\in F(X)$ put $\tau^\xi_T(f)=F(f)(\xi)$; since $F$ is a
contravariant functor, $F(f\circ g)=F(g)\circ F(f)$, so $\tau^\xi$ is a
natural transformation $h_X\to F$, and $\tau^\xi_X(\mathrm{id}_X)=\xi$. So
the map is surjective. Naturality: for $g:X'\to X$ over $S$, the
transformation $\tau\circ h_g$ is sent to
$\tau_{X'}(g)=F(g)(\xi_\tau)$; and for $\eta:F\to F'$, the transformation
$\eta\circ\tau$ is sent to $\eta_X(\xi_\tau)$.
