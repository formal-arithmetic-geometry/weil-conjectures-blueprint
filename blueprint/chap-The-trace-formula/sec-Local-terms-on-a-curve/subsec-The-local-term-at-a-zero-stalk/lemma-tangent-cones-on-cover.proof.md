+++
kind = "proof"
of = "lemma-tangent-cones-on-cover"
order = 985
uses = ["lemma-covers-degree-prime-to-ell", "lemma-tangent-cones-on-cover--1", "lemma-tangent-cones-on-cover--2"]
+++
The two covers descend to finite flat morphisms $C_i'\to C_i$ of degree $d$
between smooth curves, where $C_i$ is an étale neighbourhood of $y$ in
$X$, étale away from $y$ and with a single point $y_i'$ over $y$
(Lemma [lemma-covers-degree-prime-to-ell](1)). Their product $C_1'\times C_2'\to C_1\times C_2$ is a finite flat morphism of degree $d^2$
of smooth surfaces, étale away from the two fibres through $y$, with
$y'$ the only point over $(y,y)$. Base change to the strict localization
$T$ of $C_1\times C_2$ at $(y,y)$ gives a scheme finite over $T$ with one
point over the closed point, hence local and strictly henselian, and this
is $T'$. This proves the assertions about $T'$ and $T'\to T$.

Choose uniformizers $\xi$ of $X_1'$ and $\eta$ of $X_2'$, so that the completed
local ring of $T'$ at $y'$ is $k[[\xi,\eta]]$. Since the residue field $k$
is algebraically closed, both covers are totally ramified, so $u$ is a unit
of $k[[\xi]]$ times $\xi^d$, and similarly for $v$. Multiplying $\xi$ and
$\eta$ by suitable $d$th roots of nonzero constants, we may assume that

$$
u\equiv\xi^d,\qquad v\equiv\eta^d\pmod{(\xi,\eta)^{d+1}}.
$$

Since $\Phi_X^m$ is purely inseparable of degree $q^m$ and fixes $y$, we
have $\operatorname{ord}_v\varphi=q^m>1$, and hence
$\varphi(v)\in(\eta)^{dq^m}\subseteq(\xi,\eta)^{d+1}$. It follows that the
pulled-back equations of $\Gamma'$, $V'$, $\Delta'$ and $H'$ have initial
forms

$$
\xi^d,\qquad\xi^d,\qquad\xi^d-\eta^d,\qquad\eta^d,
$$

respectively. The support of the tangent cone of a curve is the zero set of
the initial form of its equation, and it does not change when we pass to
the reduction, since if $J$ is the radical of $I$ and $J^n\subset I$ then
the ideals of initial forms satisfy $\mathrm{in}(J)^n\subset\mathrm{in}(I)
\subset\mathrm{in}(J)$. Thus the tangent cone of
$(\Gamma'\cup V')_{\mathrm{red}}$ is supported on the line $\xi=0$, that
of $H'_{\mathrm{red}}$ on $\eta=0$, and that of $\Delta'_{\mathrm{red}}$
on the lines $\xi=\zeta\eta$ with $\zeta^d=1$. This holds also when
$p\mid d$ and $\xi^d-\eta^d$ is a $p$th power. Away from the origin the
first support meets neither of the others. Finally $H'_{\mathrm{red}}$
is the curve $\eta=0$, which is regular.
