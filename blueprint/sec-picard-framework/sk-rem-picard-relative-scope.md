+++
id = "sk-rem-picard-relative-scope"
kind = "remark"
title = "Ground fields and relative representability"
order = 875
tags = ["sketch"]
+++
For a smooth proper geometrically connected curve $C/k$ over an
arbitrary field, its degree-zero fppf Picard functor is represented by an
abelian variety $J/k$, and $J_K$ is the Jacobian of $C_K$. This is the
classical Jacobian descent theorem, stated precisely in Milne, *Jacobian
Varieties*, Theorem 1.1 and Proposition 1.9 (in this blueprint, by Galois
descent: [sk-prop-jacobian-descent]). If $C(k)$ is nonempty,
rigidification gives $J(k)=\operatorname{Pic}^0(C)$. Without a rational
point this identification need not hold; the applications use only
geometric points.

Over a general base, a separate relative theorem says that
$\operatorname{Pic}_{C/S}$ is an algebraic space if $C\to S$ is proper,
flat and of finite presentation and satisfies the condition $(\ast)$ of
the rigidification lemma ($\cO_T\to f_{T,*}\cO_{C_T}$ an isomorphism)
universally; see Stacks Project, Tag 0D2C. A smooth proper curve with
geometrically connected fibres satisfies this structure-sheaf condition.
The curve calculations use only the field case proved above
([sk-thm-picard-main]), where the Picard functor is a scheme.
