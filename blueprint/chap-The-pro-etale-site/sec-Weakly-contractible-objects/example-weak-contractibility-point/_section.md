+++
id = "example-weak-contractibility-point"
kind = "example"
title = "Weak contractibility over a point"
order = 77
uses = ["proposition-pro-etale-site-separably-closed"]
+++
Let $X$ be a geometric point, so that the affine objects of $X_{\mathrm{pro}\acute{e}t}$
are the profinite sets
(Proposition [proposition-pro-etale-site-separably-closed] below). A
continuous surjection $S\to T$ of profinite sets is a covering, so $h_S\to h_T$
is an epimorphism, and by the Yoneda lemma a section of it is a continuous
map $T\to S$ that is a section of the surjection. If $T$ is finite, such a
section exists: choose a preimage of each point; it is continuous because
$T$ is discrete. If $T=\{1,2,3,\ldots\}\cup\{\infty\}$ is a convergent
sequence, it need not exist. Let $S=T_0\amalg T_1$, where $T_0$ is the
convergent sequence $\{2,4,6,\ldots\}\cup\{\infty_0\}$ and $T_1$ is
$\{1,3,5,\ldots\}\cup\{\infty_1\}$, and map $S\to T$ by the identity on
integers and $\infty_0,\infty_1\mapsto\infty$. A section must send each
integer $n$ to its only preimage $n$, and then the even integers converge to
$\infty_0$ while the odd ones converge to $\infty_1$, so no value at $\infty$
makes the section continuous. Hence $T$ is not weakly contractible. In
agreement with Gleason's theorem, $T$ is not extremally disconnected: the
set of odd integers is open, and its closure, which contains $\infty$, is
not open, because every neighbourhood of $\infty$ contains even integers.
