+++
id = "det-ctf-finite-proper-localizing"
kind = "lemma"
title = "Finite-coefficient proper direct image on the localizing categories"
order = 2288
uses = ["det-ctf-finite-proper-tor", "lem-amb-proper-coproducts", "sk-prop-ctf-finite-comparison", "sk-thm-properbasechange"]
+++
Let $A$ be a finite $\ell$-primary ring and $p\colon X\to Y$ proper.

1. $Rp_*\colon\D(X_{\mathrm{proét}},A)\to\D(Y_{\mathrm{proét}},A)$ maps $\Dctf(X,A)$ into $\Dctf(Y,A)$ and restricts to an exact
   functor $\Loc(\Dctf(X,A))\to\Loc(\Dctf(Y,A))$ preserving arbitrary direct sums.
2. For a cartesian square with $p$ proper as in [sk-prop-proper-base-change-unbounded], the base change map
   $g^*Rp_*K\to Rp'_*g'^*K$ is an isomorphism for every $K\in\Loc(\Dctf(X,A))$.
3. For an open immersion $j$, $j_!$ preserves $\Dctf(-,A)$ and arbitrary sums, hence restricts to the
   localizing categories; so for a compactification $f=p\circ j$, $Rp_*j_!$ has the properties of (1).
