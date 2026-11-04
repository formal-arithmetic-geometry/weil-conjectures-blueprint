+++
kind = "proof"
of = "proposition-inverting-ell-full-derived-categories"
order = 301
+++
A functor with a fully faithful right adjoint is the Verdier localization
at its kernel, so we show that restriction of scalars is fully faithful
and compute the kernel.

Inverting $\ell$ is a filtered colimit along multiplication by $\ell$,
hence exact. Therefore $E_X=\mathcal O_{E,X}[1/\ell]$ is flat over
$\mathcal O_{E,X}$, and $H^q(E_X\otimes K)=H^q(K)[1/\ell]$. Restriction of
scalars is right adjoint to extension of scalars, and the counit is an isomorphism,
because $\ell$ already acts invertibly on an $E_X$-module. Restriction is
therefore fully faithful, and extension of scalars is the Verdier localization
at its kernel. By the formula for $H^q(E_X\otimes K)$, this kernel consists of
the complexes $K$ with $H^q(K)[1/\ell]=0$ for all $q$.
