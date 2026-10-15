+++
kind  = "proof"
of    = "det-thm-sfb-rationalization-comparison-verdier"
+++
Write $\mathcal T=D(X_{\mathrm{proét}},\cO_E)$ and $\mathcal T'=D(X_{\mathrm{proét}},E)$.

(1) By [det-prop-sfb-qlbar-colimit-x-invert-ell], $E_X=\varinjlim(\cO_{E,X}\xrightarrow{\ell}\cO_{E,X}\to\cdots)$
is flat over $\cO_{E,X}$, so $E_X\otimes_{\cO_{E,X}}-$ is exact on modules, preserves
quasi-isomorphisms and acyclic complexes, and computes the derived functor termwise. Exact
functors commute with cohomology, so $H^q(FK)=E_X\otimes H^q(K)=\varinjlim(H^q(K)\xrightarrow{\ell}H^q(K)\to\cdots)=H^q(K)[1/\ell]$.
A complex is zero in $\mathcal T'$ iff all its cohomology sheaves vanish, so $\ker F=\mathcal N$;
the kernel of an exact functor is a thick triangulated subcategory.

(2) On modules, $\Hom_{E_X}(E_X\otimes_{\cO_{E,X}}M,N)=\Hom_{\cO_{E,X}}(M,N)$ for an
$\cO_{E,X}$-module $M$ and an $E_X$-module $N$; both functors are exact, so the adjunction
passes to derived categories (applied to complexes termwise; homotopies and
quasi-isomorphisms are preserved by both functors). For an $E_X$-module $N$, the counit
$E_X\otimes_{\cO_{E,X}}N\to N$ is the map
$\varinjlim(N\xrightarrow{\ell}N\to\cdots)\to N$ given by $\ell^{-m}$ on the $m$-th term; since
$\ell$ acts invertibly on $N$ all transition maps are isomorphisms and this map is an
isomorphism. Hence the counit $FG\to\mathrm{id}$ is an isomorphism on complexes, and a
right adjoint with invertible counit is fully faithful.

(3) *Essential surjectivity.* Every $Y\in\mathcal T'$ is $F(G(Y))$ up to isomorphism.

*Full faithfulness.* Let $\eta\colon\mathrm{id}\to GF$ be the unit. By the triangle
identity $\varepsilon_{F}\circ F(\eta)=\mathrm{id}_F$ and (2), $F(\eta_K)$ is an isomorphism,
so the cone of $\eta_K$ lies in $\ker F=\mathcal N$, and $\eta_K$ becomes invertible in
$\mathcal T/\mathcal N$. Objects of the form $G(Y)$ are $\mathcal N$-local: for
$N\in\mathcal N$, $\Hom_{\mathcal T}(N,G(Y))=\Hom_{\mathcal T'}(F(N),Y)=0$. For an
$\mathcal N$-local object $L'$ the quotient functor induces
$\Hom_{\mathcal T}(K,L')\cong\Hom_{\mathcal T/\mathcal N}(K,L')$ (a roof $K\xleftarrow{s}K'\to L'$
with cone of $s$ in $\mathcal N$ is equivalent to a unique morphism $K\to L'$, since
$\Hom(-,L')$ inverts $s$). Hence, for $K,L\in\mathcal T$,
$$
\Hom_{\mathcal T/\mathcal N}(K,L)\cong\Hom_{\mathcal T/\mathcal N}(K,GF(L))
\cong\Hom_{\mathcal T}(K,GF(L))\cong\Hom_{\mathcal T'}(F(K),F(L)),
$$
the first map by composition with the invertible $\eta_L$, the last by adjunction. Unwinding,
the composite is the map induced by $\bar F$. So $\bar F$ is an equivalence.
