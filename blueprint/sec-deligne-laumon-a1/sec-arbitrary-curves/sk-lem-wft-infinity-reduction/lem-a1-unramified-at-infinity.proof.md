+++
kind  = "proof"
of    = "lem-a1-unramified-at-infinity"
+++
Choose a closed point of $W_0$ and a finite extension of the constant
field over which it has a rational point $s\in W$. Over this extension
choose $\tau\in\mathrm{PGL}_2$ with $\tau(s)=\infty$. Since $\tau$ is
an automorphism of $\mathbf P^1$, the set
$V_0=\tau(W_0\setminus\{s\})$ is a dense open of
$\mathbf P^1\setminus\{\infty\}=\mathbf A^1$; let $\mathcal E$ be the
transport of $\mathcal F|_{W_0\setminus\{s\}}$ by $\tau$.
It extends lisse across infinity, since $\mathcal F$ was lisse at
$s$; hence its inertia there is trivial.
Restriction to a dense open preserves geometric irreducibility:
the fundamental group of that open surjects onto the fundamental
group of the original smooth curve, by
[lem-wf-dense-open-pi1-surjective] (parts (1) and (4)).
The isomorphism $\tau$ and restriction preserve the local
weight condition of [def-weil-punctual-weights].

Open–closed recollement, [def-weil-open-closed-recollement], whose triangle exists for
$\Qlb$-Weil sheaves by [prop-sf-open-closed-triangle-all-stages],
and the vanishing of $H_c^1$ on the single point from
[lem-a1-finite-boundary-cohomology] give a surjection
$H_c^1(W\setminus\{s\},\mathcal F)\to H_c^1(W,\mathcal F)$.
Transport by $\tau$ gives the asserted map in the convention of
[def-weil-ordinary-compact-cohomology]. Every construction is defined
over the chosen finite field, so the map commutes with its Frobenius.
