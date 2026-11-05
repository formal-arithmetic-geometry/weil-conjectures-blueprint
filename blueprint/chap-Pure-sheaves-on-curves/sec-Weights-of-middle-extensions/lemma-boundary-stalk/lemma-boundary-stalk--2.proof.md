+++
kind = "proof"
of = "lemma-boundary-stalk--2"
order = 1173003
uses = ["theorem-pro-etale-refinements-weakly-etale"]
+++
Put $X=X_0\times_{\Fq}\Fbar$, $U=U_0\times_{\Fq}\Fbar$, and write
$\bar j:U\hookrightarrow X$ for the base change of $j$.
The local rings of $X$ are regular, since $X$ is smooth over $\Fbar$.
The projection $X\to X_0$ is flat, so it lifts generizations and sends
generic points to generic points. A dense open of the locally
Noetherian scheme $X_0$ contains all its generic points. It follows
that $\bar j$ has dense image; it is also quasi-compact.

We prove that the unit is an isomorphism for the underlying lisse
$\ell$-adic sheaf on $X$. For the constant sheaf
$\overline{\mathbf Q}_{\ell,X}$, its sections over a weakly étale
$T\to X$ are continuous functions $T\to\overline{\mathbf Q}_\ell$
whose values locally span a finite-dimensional $\mathbf Q_\ell$-space.
The local rings of $T$ are domains: by
[theorem-pro-etale-refinements-weakly-etale], weakly étale algebras admit
faithfully flat ind-étale refinements, and the local rings of these
refinements are filtered colimits of domains coming from étale
algebras over regular rings.

Every point of $T$ is a specialization of a point of $T\times_XU$,
and any two generizations of a point of $T$ have a common
generization. A continuous function on $T\times_XU$ therefore has at
most one extension, and its value at a point of $T$ is forced by any
such generization. This defines an extension: the clopen balls in
$\overline{\mathbf Q}_\ell$ give continuity, and quasi-compactness of
$\bar j$ preserves the local finite-dimensional condition. Thus
restriction from $T$ to $T\times_XU$ is bijective on these sections.
This is the constant-sheaf case of the unit isomorphism.

A lisse sheaf becomes a finite direct sum of copies of
$\overline{\mathbf Q}_\ell$ on a pro-étale cover. The preceding
argument applies over each member of this cover and passes to finite
direct sums. Restrictions to a covering family jointly detect
isomorphisms, so the unit is an isomorphism for the lisse sheaf on
$X$. This is
`AlgebraicGeometry.ProEtale.IsAdicLisseSheaf.isIso_adicUpperStarLowerStarAdjunction_unit_app`.

Finally, the unit for Weil sheaves has this adic unit as its underlying
morphism and respects the Weil structures. The forgetful functor
reflects isomorphisms, giving the asserted isomorphism of Weil
sheaves.
