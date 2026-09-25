+++
id = "sk-input-weights"
kind = "section"
title = "The weight estimate: Deligne purity"
order = 3148
uses = ["sk-cor-dl-general-complex", "sk-d-dl-general-weights", "sk-d-real-weights", "sk-def-cohfamily", "sk-def-roots", "sk-p-real-purity", "sk-prop-sf-comp-proper", "sk-prop-smooth-proper-purity", "sk-thm-dl-a1-upper", "sk-thm-dl-general-sheaf", "sk-thm-poincare-duality"]
+++
*Proposition (sketch).*

Let $X_0/k_0$ be smooth, proper and geometrically connected of pure dimension
$d$, and suppose the structure morphism is exceptional-adjoint admissible.
Then for every $0\le i\le2d$:

1. the constant Weil sheaf is $\iota$-pure of weight $0$;
1. $H_c^{i}(X,\Qlb)$ is $\iota$-mixed of weights $\le i$;
1. the comparison $H_c^{i}(X,\Qlb)\to H^{i}(X,\Qlb)$ is
Frobenius-equivariant;
1. $V_{i,\ell}=H^{i}(X,\Ql)$ is $\iota$-pure of weight $i$;
1. every eigenvalue $\alpha$ of geometric Frobenius on $V_{i,\ell}$
satisfies $|\iota(\alpha)|=q^{i/2}$.

The relative form is the estimate for $Rf_{!}$: for a separated finite-type
morphism of relative dimension $\le1$ and a pure lisse coefficient sheaf, $Rf_!$
carries weights $\le w$ to weights $\le w+\text{(relative dimension)}$.

## Proof

Clauses (1) and (3) are formal, clause (2) and the relative estimate are
[sk-thm-dl-general-sheaf], and clauses (4)–(5) follow from
[sk-prop-smooth-proper-purity].

*(1)* At a closed point $x$ the constant Weil sheaf has
$P_x\bigl((\Qlb)_{X_0},T\bigr)=1-T$, so its only local eigenvalue is $1$ and
[sk-d-real-weights] gives weight $0$.

*(2)* Apply [sk-thm-dl-general-sheaf] to the structure morphism
$a_{X_0}:X_0\to\Spec k_0$ and to the constant sheaf, which is mixed of
weights at most $0$ by (1): $H_c^{i}(X,\Qlb)=R^{i}a_{X_0!}(\Qlb)_{X_0}$ is
$\iota$-mixed of weights at most $i$.

*(3)* $X_0$ is proper, so $Ra_{X_0!}\to Ra_{X_0*}$ is an isomorphism
by [sk-prop-sf-comp-proper], and it is a map of Weil data; hence
$H_c^{i}(X,\Qlb)\to H^{i}(X,\Qlb)$ is a Frobenius-equivariant isomorphism.

*(4)–(5)* Apply [sk-prop-smooth-proper-purity] to
$a_{X_0}:X_0\to\Spec k_0$, which is smooth and proper of pure relative
dimension $d$, and to $\mathcal F_0=(\Ql)_{X_0}$, pure of weight $0$ by (1).
Clause (b) of that proposition, in the absolute form of its Step 4, says
that $V_{i,\ell}=H^{i}(X,\Ql)$ is $\iota$-pure of weight $i$ and that every
eigenvalue $\alpha$ of geometric Frobenius on it satisfies
$|\iota(\alpha)|=q^{i/2}$. These are (4) and (5). The only duality used is
[sk-thm-poincare-duality] (5), so this step adds nothing beyond (2).
Both conclusions hold for every choice
of $\iota$, since $\iota$ was arbitrary in (2) and in
[sk-prop-smooth-proper-purity].

*The relative form.* The estimate quoted for $Rf_!$ in the statement
is [sk-thm-dl-general-sheaf] for sheaves and
[sk-cor-dl-general-complex] for bounded complexes; the relative-dimension
restriction in the statement is the inductive case, whose affine-line core
is [sk-thm-dl-a1-upper] of §[sec-deligne-laumon-a1] and whose
real-sheaf input is [sk-p-real-purity] of
§[sec-purity-real-sheaves].

Consequently the zeta layer's use of clause (5) through
[sk-prop-rootpurity] rests on [sk-thm-trace-formula],
[sk-thm-poincare-duality] and [sk-thm-dl-general-sheaf] alone. In the
detailed source the packaged statement is `thm:weil-deligne-purity`,
with the relative estimate `thm:zl-wme-deligne-estimate`.

Uses: [sk-cor-dl-general-complex], [sk-d-dl-general-weights], [sk-d-real-weights], [sk-def-cohfamily], [sk-def-roots], [sk-p-real-purity], [sk-prop-sf-comp-proper], [sk-prop-smooth-proper-purity], [sk-thm-dl-a1-upper], [sk-thm-dl-general-sheaf], [sk-thm-poincare-duality]
