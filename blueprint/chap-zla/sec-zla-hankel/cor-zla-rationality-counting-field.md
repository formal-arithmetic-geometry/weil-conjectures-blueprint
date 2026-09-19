+++
id = "cor-zla-rationality-counting-field"
kind = "theorem"
title = "Rationality over the counting field"
order = 1006
tags = ["latex:corollary"]
uses = ["def-zla-rational-germ", "thm-zla-hankel-descent"]
+++
If $Z(T)\in\mathbf Q[[T]]$ becomes the Taylor series of a normalized rational
germ after coefficientwise extension to a characteristic-zero field $E$, then
$Z(T)\in\mathbf Q(T)_0$: there are $A,B\in\mathbf Q[T]$ with $B(0)=1$ and
$B(T)Z(T)=A(T)$.

## Proof

Apply [thm-zla-hankel-descent] to the extension $\mathbf Q\subseteq E$,
which is an extension of fields because $E$ has characteristic zero.
