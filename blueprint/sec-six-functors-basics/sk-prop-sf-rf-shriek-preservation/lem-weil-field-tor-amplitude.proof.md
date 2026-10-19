+++
kind  = "proof"
of    = "lem-weil-field-tor-amplitude"
+++
Complexes of finite Tor amplitude form a subcategory closed under shifts and
cones: from a triangle $K'\to K\to K''\to$ and the long exact cohomology
sequence of $-\otimes^{\mathbf L}_{\Lambda_Y}M$, if $K'$ and $K''$ have Tor
amplitude in $[a',b']$ and $[a'',b'']$, then $K$ has Tor amplitude in
$[\min(a',a''),\max(b',b'')]$. By [sk-cor-coefficient-heart-ii], $K$ is
obtained by finitely many cones from objects $a_!L[n]$, with
$a:S\hookrightarrow Y$ a locally closed immersion and $L$ a lisse
$\Lambda_S$-module ([sk-lem-coefficient-heart] (3)), so it suffices to show
that $a_!L$ has Tor amplitude in $[0,0]$. The module $L$ is locally free of
finite rank for the pro-étale topology, hence flat, so
$L\otimes^{\mathbf L}_{\Lambda_S}N=L\otimes_{\Lambda_S}N$ for every
$\Lambda_S$-module $N$. Writing $a=i\circ u$ with $u$ open and $i$ closed, the
functors $u_!$, $i_*$ and $a^*$ are exact and satisfy the projection formulas
$u_!L\otimes M\cong u_!(L\otimes u^*M)$ and
$i_*L'\otimes M\cong i_*(L'\otimes i^*M)$, so

$$
a_!L\otimes^{\mathbf L}_{\Lambda_Y}M\cong a_!\bigl(L\otimes_{\Lambda_S}a^*M\bigr)
$$

is a sheaf in degree $0$.
