+++
kind  = "proof"
of    = "prop-wf-weil-sheaf-representation-equivalence"
uses  = ["thm-lisse-qlbar-representations", "def-wf-weil-group", "def-wf-constant-weil-twist", "sk-lem-coefficient-heart", "sk-prop-sfb-module-pullback-exact", "sk-prop-pe-condensed-point", "lem-wf-lisse-stalk-vanishing"]
+++
*Geometric level.* The curve $C$ is smooth over $k$, hence regular and
connected, so by [thm-lisse-qlbar-representations] the functor
$\mathcal F\mapsto(\mathcal F_{\bar\eta},\rho_{\mathrm{geom}})$ is an equivalence
between lisse $\overline{\mathbf Q}_{\ell,C}$-modules on $C_{\mathrm{proét}}$ (locally
free of finite rank, [sk-lem-coefficient-heart]) and continuous finite-dimensional
$\Qlb$-representations of $P$, each defined over some finite $E/\Ql$; rank is the
dimension of the stalk and is constant because $C$ is connected. Lattices,
reductions modulo $\mathfrak m_E^n$ and limits enter only inside the proof of
[thm-lisse-qlbar-representations].

*Frobenius descent.* Geometric Frobenius is an automorphism of the
scheme $C$, so $\Frob^*$ is an autoequivalence of lisse sheaves on $C$;
comparing the stalks at $\bar\eta$ and $\Frob(\bar\eta)$ along the
degree-one lift $\gamma$ turns it into a twist of $\rho$ by the conjugation
$c_\gamma(g)=\gamma g\gamma^{-1}$ of $P$, and the comparison is oriented
so that the twist is $\rho\mapsto\rho\circ c_\gamma^{-1}$,
$g\mapsto\rho(\gamma^{-1}g\gamma)$ (the opposite orientation amounts to
replacing $\gamma$ by the degree $-1$ lift $\gamma^{-1}$). A Weil
structure $\varphi:\Frob^*\mathcal F\to\mathcal F$ is therefore an
automorphism $\Phi$ of $V$ with
$\Phi\,\rho(g)\,\Phi^{-1}=\rho(\gamma g\gamma^{-1})$ for $g\in P$, which is
exactly the relation making $g\gamma^{n}\mapsto\rho(g)\Phi^{n}$
multiplicative; since every element of $W(C_0)$ is uniquely $g\gamma^{n}$
by [def-wf-weil-group], setting $\rho(\gamma)=\Phi$ extends $\rho$ to
$W(C_0)$. (With the relation written as
$\Phi\,\rho(\gamma g\gamma^{-1})\,\Phi^{-1}=\rho(g)$ one would be forced to
set $\rho(\gamma)=\Phi^{-1}$ instead.) The choice $\rho(\gamma)=\Phi$ is
the geometric Frobenius normalization of [def-wf-weil-group]: at a closed
point $x$ with $k(x)=\Fq$ the operator induced by $\varphi$ on
$\mathcal F_{\bar x}$ is the geometric Frobenius $F_x$, because $\Frob$
composed with the arithmetic Frobenius of $k$ is the absolute Frobenius of
$C$, which acts trivially on étale and pro-étale sheaves, and $F_x$ has degree $+1$; so
the degree-one elements $g\gamma$ of $W(C_0)$ act through $\Phi$, not
$\Phi^{-1}$, in agreement with $F=\rho(\gamma)$ and with the Tate line
$\Qlb(1)=\mathcal B_{q^{-1}}$ (geometric Frobenius acts on $\Qlb(1)$ by
$q^{-1}$), in the notation of the constant Weil twist
[def-wf-constant-weil-twist]. Another lift changes
$\Phi$ by an element of $\rho(P)$ and gives an isomorphic representation. The
morphism condition $u\varphi=\psi\,\Frob^{*}u$ says on stalks that $u$
intertwines the two operators $\Phi$, which with $P$-equivariance is exactly
$W(C_0)$-equivariance; hence full faithfulness.

*Exactness.* Kernels and cokernels of maps of lisse Weil sheaves are formed in
$\Mod(C_{\mathrm{proét}},\Qlb)$, where they are constructible
([sk-lem-coefficient-heart] (1)), and the Weil structures pass to them. Geometric stalks
are exact (for a geometric point $s:\Spec K\to C$ the pullback $s^*$ is exact by
[sk-prop-sfb-module-pullback-exact], and
$\Gamma(\Spec K,-)$ is exact because every pro-étale cover of $\Spec K$ has a section,
[sk-prop-pe-condensed-point]), monoidal, and jointly conservative on $\Cons(C,\Qlb)$: if all
stalks of a constructible $M$ vanish, then for each stratum $a:S\hookrightarrow C$ of the
filtration of [sk-lem-coefficient-heart] (3) the restriction $a^*M$ is lisse with vanishing
stalks, hence zero by [lem-wf-lisse-stalk-vanishing] (2); so every subquotient $a_!(a^*M)$
of the filtration vanishes, and $M=0$. For lisse
sheaves on the connected $C$ the stalk at any geometric point is identified with the
stalk at $\bar\eta$, naturally in the sheaf, by an isomorphism of fibre functors.
Hence a sequence of lisse Weil sheaves is short exact if and only if the sequence of
geometric generic stalks is, and tensor products correspond. The matching of
subobjects, quotients and subquotients follows.
