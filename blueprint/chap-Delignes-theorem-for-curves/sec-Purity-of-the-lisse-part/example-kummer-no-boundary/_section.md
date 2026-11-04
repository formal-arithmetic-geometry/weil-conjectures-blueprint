+++
id = "example-kummer-no-boundary"
kind = "example"
title = "A Kummer sheaf has no boundary term"
order = 1269
uses = ["lemma-boundary-stalk"]
+++
Let $M$ be the Kummer sheaf of a nontrivial character $\chi$ on
$U_0=\mathbf G_m$. It is irreducible and pure of weight $0$. It is tame
at infinity, so it has no geometric constituent $\mathcal L_{\psi(ax)}$,
and it satisfies the hypotheses of this subsection. Inertia at the
origin acts on $M$ through $\chi$, nontrivially. Hence
$(j_*M)_{\bar0}=0$ by Lemma [lemma-boundary-stalk]. This means that
$j_!M=j_*M$ and $B=0$, and the lemma gives $G\simeq j'_*M'$. On
$\mathbf F_q$-points this is visible. By (16.3) the trace
of $G$ at $y\ne0$ is $-\sum_x\chi(x)\psi(xy)=-\overline\chi(y)g$, with
$g=\sum_x\chi(x)\psi(x)$. For the quadratic character this is the trace
of $M'$ computed at the start of Section [chap-Delignes-theorem-for-curves].
At $y=0$ the trace of $G$ is $-\sum_x\chi(x)=0$, in agreement with
$H^1_c(\mathbf G_m,M)=0$.
