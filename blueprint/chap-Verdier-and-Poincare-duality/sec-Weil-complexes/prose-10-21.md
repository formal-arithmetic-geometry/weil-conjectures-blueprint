+++
id = "prose-10-21"
kind = "hidden"
title = "Weil complexes (3)"
order = 879
+++
When $T$ and $K$ are clear, we write $F$ for [$\operatorname{Frob}_{T,K}$](@definition-frobenius-operator) and
for the endomorphisms it induces on the groups $H^i_c(T,K)$.

For $r\in\mathbf Z$, write
$\Lambda(r)=\Gamma(\href{@definition-small-pro-etale-site}{(\operatorname{Spec}k)_{\mathrm{pro}\acute{e}t}},
\href{@definition-tate-twists}{\Lambda_{\operatorname{Spec}k}(r)})$ for the Tate coefficient
module with its induced [Frobenius operator](@definition-frobenius-operator). Arithmetic Frobenius
acts on $\mu_{\ell^n}(k)$ by $\zeta\mapsto\zeta^q$. Hence geometric Frobenius
acts on [$\Lambda(1)$](@definition-tate-twists) by $q^{-1}$, and on [$\Lambda(-d)$](@definition-tate-twists) by $q^d$.
Let $X_0$ be smooth of pure dimension $d$. After removing the twist, the
trace map of Definition [definition-trace-map] is a Frobenius-equivariant
map, by Proposition [proposition-purity-trace-commute-frobenius] below:

$$
H_c^{2d}(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},\Lambda_X)\longrightarrow\href{@definition-tate-twists}{\Lambda(-d)}.
$$

For $X=\mathbf P^1_k$ this says that geometric Frobenius acts on
$H^2(\mathbf P^1_k,\Lambda)=\href{@definition-tate-twists}{\Lambda(-1)}$ by $q$, as checked after
Proposition [proposition-adjunction-projective-line].
