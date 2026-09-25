+++
id = "sk-d-trace-class"
kind = "section"
title = "Diagonal trace class"
order = 2438
uses = ["sk-d-corr", "sk-d-pairing"]
+++
*Definition (sketch).*

For $(X,K)$, the diagonal identity is the
endocorrespondence with support $X$, support map
$\Delta_X:X\to X\times X$, identity legs, and coefficient map $1_K$.
For another endocorrespondence $(C,c,u)$, its intersection with this
diagonal is $F=\Fix(c)$. Define its trace class by the
supported pairing:

$$
\Tr_c(u):=\langle u,1_K\rangle_{\mathrm{LV}}:A_F\longrightarrow\omega_F.
$$

This is a class on the specified scheme $F$; integration, when defined,
is a separate operation.

Uses: [sk-d-corr], [sk-d-pairing]
