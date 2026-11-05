+++
id = "prose-11-16"
kind = "hidden"
title = "Additivity of trace classes (1)"
order = 930
+++
To compute local terms, we cut $K$ into pieces along a decomposition of
$X$ into an open and a closed part, both invariant under the
correspondence. For this the trace class must be additive. For
the trace of an endomorphism of a perfect complex, additivity says that
a block triangular matrix has trace equal to the sum of the traces of
its diagonal blocks. By Remark [remark-coherent-additivity] it can
only be expected for filtrations lifted to the filtered derived
category. The trace class needs the same care, and we lift each step of
the construction of the trace morphism to filtered complexes.

In a two-step filtration, for example, a filtered correspondence is a
block triangular matrix
$\left(\begin{smallmatrix}u_0&*\\0&u_1\end{smallmatrix}\right)$ whose
off-diagonal entry has weight $1$. Since $\omega_X$ sits in filtration degree
$0$, the trace class does not see this entry
(Lemma [lemma-filtered-trace-morphism] below).

The operations that enter the
trace morphism have filtered versions, with explicit formulas for their
graded pieces. We use finite decreasing filtrations, the convolution filtration on tensor
products, and the filtration on internal Hom given by

$$
F^r\mathcal Hom(\mathcal M,\mathcal N)
=\{v:v(F^a\mathcal M)\subset F^{a+r}\mathcal N
\text{ for every }a\}.
$$

Write $\cHom_F$, $\otimes_F$ and $\mathbb D_F=\cHom_F(-,\omega_X)$ for
the derived functors on the filtered derived category, where $\omega_X$
carries the filtration concentrated in weight zero, and $M_a$, $N_a$,
$K_a$ for the graded pieces of $\mathcal M$, $\mathcal N$, $\mathcal K$.
