+++
kind = "proof"
of = "lem-weil-pbc-charpoly-locally-free-existence"
+++
*Local polynomials.* For each $i$, $M_{f_i}\cong M\otimes_AA_{f_i}$, so the given basis of $M_{f_i}$ is a basis of the scalar extension; let $\chi_i\in A_{f_i}[T]$ be the characteristic polynomial of $\varphi\otimes1$ in it. It does not depend on the basis (conjugate matrices have the same characteristic polynomial), and it is monic of degree $n$.

*Towers.* For ring maps $A\to S\to T$ such that $M\otimes_AS$ and $M\otimes_AT$ are free of rank $n$, the characteristic polynomial of $\varphi_T$ is the image of that of $\varphi_S$: a basis of $M\otimes_AS$ extends to a basis of $(M\otimes_AS)\otimes_ST\cong M\otimes_AT$, in which $\varphi_T$ has the image matrix.

*Agreement on overlaps.* Applying the tower statement to $A_{f_i}\to A_{f_if_j}$ and $A_{f_j}\to A_{f_if_j}$, the images of $\chi_i$ and $\chi_j$ in $A_{f_if_j}[T]$ are both the characteristic polynomial of $\varphi$ over $A_{f_if_j}$, hence equal.

*Gluing.* Since $f_1,\dots,f_r$ generate the unit ideal, an element of $A$ is determined by its images in all $A_{f_i}$, and a family of elements $a_i\in A_{f_i}$ whose images agree in all $A_{f_if_j}$ comes from a unique $a\in A$. Applying this to each coefficient of $T^k$, $0\le k<n$, gives $c_k\in A$, and $\chi=T^n+\sum_{k<n}c_kT^k$ maps to $\chi_i$ for every $i$ (if some $A_{f_i}$ is the zero ring the condition there is empty).

*The base-change property.* Let $\rho:A\to A'$ be such that $M\otimes_AA'$ is free of rank $n$. The images $\rho(f_i)$ generate the unit ideal of $A'$. Over $T_i=A'_{\rho(f_i)}$, which is an $A_{f_i}$-algebra, the tower statement applied to $A\to A_{f_i}\to T_i$ and to $A\to A'\to T_i$ shows that the images of $\chi$ and of the characteristic polynomial of $\varphi_{A'}$ in $T_i[T]$ coincide. By injectivity of $A'\to\prod_iT_i$ (applied coefficientwise) they are equal.

*Uniqueness.* If $\chi'$ also has the base-change property, applying it to $A\to A_{f_i}$ shows that $\chi'$ maps to $\chi_i$ for every $i$, so $\chi'=\chi$ by injectivity of $A\to\prod_iA_{f_i}$ coefficientwise.

*The free case.* If $M$ is free of rank $n$, apply the base-change property to the identity of $A$: $M\otimes_AA\cong M$, and the matrix of $\varphi\otimes1$ in the transported basis is that of $\varphi$, so $\chi$ is the usual characteristic polynomial.
