+++
id = "sk-d-trace-class"
kind = "section"
title = "Diagonal trace class"
order = 2313
uses = ["sk-d-corr", "sk-d-pairing"]
lean = ["AlgebraicGeometry.ProEtale.GeometricOperations.traceClass"]
+++
*Definition (sketch).*

Let $s$ be the spectrum of a field, $X$ quasi-compact and compactifiable
over $s$, and $K\in D^b_{ctf}(X,A)$.
For $(X,K)$, the diagonal identity is the
endocorrespondence with support $X$, support map
$\Delta_X:X\to X\times X$, identity legs, and coefficient map $1_K$.
For another endocorrespondence $(C,c,u)$, its intersection with this
diagonal is $F=\Fix(c)=C\times_{X\times X}X$. Its trace class
$\Tr_c(u):A_F\to\omega_F$ is the supported pairing of $u$ against the
diagonal identity: the contraction of [sk-d-pairing] applied to the supported
classes $\widetilde u$ of $u$ and of $1_K$, carried out over the Cartesian
square $F=C\times_{X\times X}X$, so that it lands directly on $F$:

$$
\Tr_c(u)=\langle u,1_K\rangle_{\mathrm{LV}}:A_F\longrightarrow\omega_F .
$$

It agrees with the Verdier trace class (the mate of $u$ followed by the trace
map of external duality, [def-trf-trace-class]) by
[lem-trf-trace-class-diagonal-pairing].

This is a class on the specified scheme $F$; integration, when defined,
is a separate operation.
