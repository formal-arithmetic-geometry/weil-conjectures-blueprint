+++
id = "det-sp-reduction-compatibilities"
kind = "lemma"
title = "Coefficient comparisons: units, composition and purity"
order = 2924
uses = ["det-sp-reduction-direct-image", "det-sp-reduction-exceptional", "thm-pur-diagonal-dualizing-object"]
+++
In the situation of [det-sp-reduction-exceptional]:

1. *Units.* For $M\in\Dctf(X_{\mathrm{proét}},A)$, in $\Dctf(X_{\mathrm{proét}},B)$,
   $$
   f_B^!\bigl(b(M)\bigr)\circ c_{A,B}(Rf_{!,A}M)\circ (\eta_A(M))_B=\eta_B(M_B).
   $$
2. *Composition.* For $A\to B\to C$, the composite
   $(f_A^!K)_C\simeq((f_A^!K)_B)_C\xrightarrow{c_{A,B}(K)_C}(f_B^!K_B)_C
   \xrightarrow{c_{B,C}(K_B)}f_C^!((K_B)_C)\simeq f_C^!K_C$
   equals $c_{A,C}(K)$.
3. *Purity.* For $K\in\Dctf(Y_{\mathrm{proét}},A)$, in $\Dctf(X_{\mathrm{proét}},B)$,
   $$
   c_{A,B}(K)\circ (\gamma_{f,A}(K))_B=\gamma_{f,B}(K_B),
   $$
   the sources being identified by $(f_A^*K(d)[2d])_B\simeq f_B^*(K_B)(d)[2d]$.
