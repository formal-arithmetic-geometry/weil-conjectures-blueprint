+++
kind = "proof"
of = "lem-weil-pbc-flat-iso-mod-ideal-powers"
+++
Write $\beta_n:A/I^n\to B/I^nB$ for the induced map.

*Surjectivity.* Since $\beta_1$ is surjective, $B=\varphi(A)+IB$. By induction on $n$, $B=\varphi(A)+I^nB$: given $b=\varphi(a)+\sum_kx_kb_k$ with $x_k\in I^{n}$, write each $b_k=\varphi(a_k)+y_k$ with $y_k\in IB$, so that $b\in\varphi(A)+I^{n+1}B$. Hence every $\beta_n$ is surjective.

*Flatness.* $B/I^nB\cong(A/I^n)\otimes_AB$ as $A/I^n$-algebras, so $\beta_n$ is flat by base change.

*Nilpotent kernel.* Let $n\ge1$. If $\beta_n(a\bmod I^n)=0$ then $\varphi(a)\in I^nB\subseteq IB$, so $a\in I$ by injectivity of $\beta_1$. Thus $\ker\beta_n$ is contained in the image of $I$ in $A/I^n$, whose $n$-th power is zero.

*Injectivity.* For a surjective flat ring map $f:R\to R'$, $R/\ker f\cong R'$ is flat over $R$, so $\ker f$ is a pure ideal, hence idempotent; all its positive powers equal it. If moreover $\ker f$ is nilpotent, it is zero. Applied to $\beta_n$, this shows $\beta_n$ is injective, hence an isomorphism.
