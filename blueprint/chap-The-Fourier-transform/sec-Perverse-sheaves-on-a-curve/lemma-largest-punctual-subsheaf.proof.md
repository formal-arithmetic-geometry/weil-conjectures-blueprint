+++
kind = "proof"
of = "lemma-largest-punctual-subsheaf"
order = 1240
uses = ["proposition-lattices-representations-normal-scheme"]
+++
Let $L$ be a lisse sheaf. For a geometric point $\bar x$ and a
geometric generic point $\bar\eta$ specializing to it, the
generization map $L_{\bar x}\to L_{\bar\eta}$ is injective. For a
sheaf defined over a finite extension $E$ of $\mathbf Q_\ell$, this holds for the
finite locally constant reductions of the lattice in
Proposition [proposition-lattices-representations-normal-scheme], and we pass to
the inverse limit, invert the uniformizer and extend scalars. A
punctual subsheaf $G\subset L$ has $G_{\bar\eta}=0$, and since the
generization maps of $G$ and $L$ are compatible, $G_{\bar x}=0$.

Now let $F$ and $U$ be as in the statement. The sheaf $F_{\rm p}$ is
supported on the finite set $C\setminus U$, hence punctual. A
punctual subsheaf $G$ of $F$ restricts to a punctual subsheaf of the
lisse sheaf $j^*F$, hence to zero. Its map to $j_*j^*F$ is adjoint to
$j^*G\to j^*F$, so it vanishes, and $G\subset F_{\rm p}$. Finally,
$j_*j^*F$ has no nonzero punctual subsheaf. Indeed, if
$H\subset j_*j^*F$ is punctual, then $j^*H=0$, and the inclusion is zero
since $\Hom(H,j_*j^*F)=\Hom(j^*H,j^*F)=0$. As $F/F_{\rm p}$ embeds in
$j_*j^*F$, it has no nonzero punctual subsheaf either.
