+++
kind  = "proof"
of    = "lem-kun-derived-tensor-t-est"
+++
By [lem-kun-0f1m], $A$ is represented by a K-flat complex
$\mathcal A^\bullet$ of flat $\Lambda_T$-module sheaves with
$\mathcal A^p=0$ for $p<a$. Since $\mathcal H^i(B)=0$ for $i<b$, the
good truncation ([def-kun-truncations]) of any complex representing
$B$ gives a complex $\mathcal B^\bullet$ representing $B$ with
$\mathcal B^q=0$ for $q<b$. As $\mathcal A^\bullet$ is K-flat,
[def-kun-derived-tensor] gives

$$
A\kunotimes{\Lambda}B=\mathcal A^\bullet\otimes_\Lambda\mathcal B^\bullet,
\qquad
\bigl(\mathcal A^\bullet\otimes_\Lambda\mathcal B^\bullet\bigr)^n
=\bigoplus_{p+q=n}\mathcal A^p\otimes_\Lambda\mathcal B^q .
$$

A nonzero summand needs $p\ge a$ and $q\ge b$, hence $n\ge a+b$. So the
total complex vanishes in degrees $<a+b$, and so does its cohomology.
