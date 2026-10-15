+++
id = "sk-lem-sp-tower-bound"
kind = "lemma"
title = "Direct image preserves constructible towers"
order = 1837
uses = ["sk-def-sp-normalized-towers", "sk-lem-sp-tower-levels", "sk-thm-sf-ctf-stability"]
tags = ["sketch"]
+++
Let $f:X\to Y$ be smooth of pure relative dimension $d$ (the argument only uses
that $f$ is separated of finite type with fibres of dimension $\leq d$), with a
compactification $f=\bar f\circ j$, and put
$Rf_{!,\bullet}=R\bar f_{*,\bullet}\circ j_{!,\bullet}:
D^+(\operatorname{Tow}(X,\mathcal O_E))\to D^+(\operatorname{Tow}(Y,\mathcal O_E))$, where
$j_{!,\bullet}$ is levelwise extension by zero; by [sk-lem-sp-tower-levels],
$(Rf_{!,\bullet}C_\bullet)_n\simeq Rf_{!,\mathcal O_E/\ell^n}C_n$. For
$C_\bullet\in\Dctf(X_{\mathrm{proét}},\mathcal O_E/\ell^\bullet)$, one has
$Rf_{!,\bullet}C_\bullet\in\Dctf(Y_{\mathrm{proét}},\mathcal O_E/\ell^\bullet)$.
