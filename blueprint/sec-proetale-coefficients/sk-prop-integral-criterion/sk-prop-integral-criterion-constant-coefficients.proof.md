+++
kind  = "proof"
of    = "det-prop-integral-criterion-constant-coefficients"
+++
(1) This is \stacks{099L}. Concretely: $\cO_{E,X}$ is $\pi_E$-torsion free, being a limit of
the sheaves $(\cO_E/\pi_E^n)_X$ along which multiplication by $\pi_E$ is compatible with
the injections $\cO_E/\pi_E^{n-1}\xrightarrow{\pi_E}\cO_E/\pi_E^n$. On the pro-étale site
the limit along the surjections $(\cO_E/\pi_E^{n+1})_X\to(\cO_E/\pi_E^n)_X$ has
$\varprojlim^1=0$ and surjective projections (repleteness), so
$0\to\cO_{E,X}\xrightarrow{\pi_E^n}\cO_{E,X}\to(\cO_E/\pi_E^n)_X\to0$ is exact (it is the
limit of the exact sequences
$0\to\cO_E/\pi_E^{m}\xrightarrow{\pi_E^n}\cO_E/\pi_E^{m+n}\to\cO_E/\pi_E^n\to0$). This is
the isomorphism modulo $\pi_E^n$. Flatness: a sheaf $M$ of modules over the constant sheaf
$(\cO_E)_X$ is a sheaf with an $\cO_E$-action, and $M\otimes_{(\cO_E)_X}N$ is the
sheafification of the presheaf $U\mapsto M(U)\otimes_{\cO_E}N(U)$. Since multiplication by
$\pi_E$ is injective on $\cO_{E,X}$, it is injective on every group of sections
$\cO_{E,X}(U)$ (sections are left exact). A torsion-free module over the discrete
valuation ring $\cO_E$ is flat. Since $-\otimes_{(\cO_E)_X}-$ is right exact, it suffices to
see that it preserves monomorphisms $N'\hookrightarrow N$: these are injective on sections,
so $\cO_{E,X}(U)\otimes_{\cO_E}N'(U)\to\cO_{E,X}(U)\otimes_{\cO_E}N(U)$ is injective for every
$U$, and sheafification preserves injectivity. Hence $\cO_{E,X}\otimes_{(\cO_E)_X}-$ is exact.

(2) and (3). A ring map $c$ which is flat and an isomorphism modulo $\pi_E^n$ for all $n$
induces, by \stacks{099I}, an equivalence between derived complete objects as stated. The
reason: for $K$ over $\cO_{E,X}$, flatness gives
$K\otimes^{\mathbf L}_{(\cO_E)_X}(\cO_E)_X/\pi_E^n=K\otimes^{\mathbf L}_{\cO_{E,X}}\cO_{E,X}/\pi_E^n$
by (1), which is (3); derived completeness is the condition
$K\cong\operatorname{R\lim}_nK\otimes^{\mathbf L}\cO/\pi_E^n$ (derived Nakayama and the
limit description of [sk-def-pe-derived-completion]), and both the condition and the
reductions agree on the two sides. Hence restriction of scalars is fully faithful on
complete objects (Hom between complete objects is the $\operatorname{R\lim}$ of Hom between
reductions, which agree) and essentially surjective (the inverse functor displayed is
complete, and its reductions are those of $L$ by (1)).
