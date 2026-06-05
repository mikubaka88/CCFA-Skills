%%
%% This is file `siamltex.cls', based on article.cls
%% Revision of siam macros for use with LaTeX 2e
%%
%% By Paul Duggan for the Society for Industrial and Applied
%% Mathematics.
%%
%% November 13, 1996
%%
%% Version 1.2.1
%%
%% You are not allowed to change this file.
%%
%% You are allowed to distribute this file under the condition that
%% it is distributed together with all of the files in the siam macro
%% distribution. These are:
%%
%%  siamltex.cls (this file)
%%  siamltex.sty (includes siamltex.cls for compatibility mode)
%%  siam10.clo   (size option for 10pt papers)
%%  subeqn.clo   (allows equation numbners with lettered subelements)
%%  siam.bst     (bibliographic style file for BibTeX)
%%  docultex.tex (documentation file)
%%  lexample.tex (example file for latex macro)
%%
%% If you receive only some of these files from someone, complain!
%%
%% You are NOT ALLOWED to distribute this file alone. You are NOT
%% ALLOWED to take money for the distribution or use of either this
%% file or a changed version, except for a nominal charge for copying
%% etc.
%% \CharacterTable
%%  {Upper-case    \A\B\C\D\E\F\G\H\I\J\K\L\M\N\O\P\Q\R\S\T\U\V\W\X\Y\Z
%%   Lower-case    \a\b\c\d\e\f\g\h\i\j\k\l\m\n\o\p\q\r\s\t\u\v\w\x\y\z
%%   Digits        \0\1\2\3\4\5\6\7\8\9
%%   Exclamation   \!     Double quote  \"     Hash (number) \#
%%   Dollar        \$     Percent       \%     Ampersand     \&
%%   Acute accent  \'     Left paren    \(     Right paren   \)
%%   Asterisk      \*     Plus          \+     Comma         \,
%%   Minus         \-     Point         \.     Solidus       \/
%%   Colon         \:     Semicolon     \;     Less than     \<
%%   Equals        \=     Greater than  \>     Question mark \?
%%   Commercial at \@     Left bracket  \[     Backslash     \\
%%   Right bracket \]     Circumflex    \^     Underscore    \_
%%   Grave accent  \`     Left brace    \{     Vertical bar  \|
%%   Right brace   \}     Tilde         \~}
\NeedsTeXFormat{LaTeX2e}[1995/06/01]
\ProvidesClass{siamltex}[1996/10/11 v1.2 LaTeX document class]
\newcommand\@ptsize{}
\newif\if@restonecol
\newif\if@titlepage
\@titlepagefalse
\newif\if@oneeqnum
\@oneeqnumfalse
\newif\if@onetabnum
\@onetabnumfalse
\newif\if@onefignum
\@onefignumfalse
\newif\if@onethmnum
\@onethmnumfalse
%_%_%_%_%
\newif\if@translated
\@translatedfalse
%_%_%_%_%
%\newif\if@openbib
%\@openbibfalse
\DeclareOption{a4paper}
   {\setlength\paperheight {297mm}%
    \setlength\paperwidth  {210mm}}
\DeclareOption{a5paper}
   {\setlength\paperheight {210mm}%
    \setlength\paperwidth  {148mm}}
\DeclareOption{b5paper}
   {\setlength\paperheight {250mm}%
    \setlength\paperwidth  {176mm}}
\DeclareOption{letterpaper}
   {\setlength\paperheight {11in}%
    \setlength\paperwidth  {8.5in}}
\DeclareOption{legalpaper}
   {\setlength\paperheight {14in}%
    \setlength\paperwidth  {8.5in}}
\DeclareOption{executivepaper}
   {\setlength\paperheight {10.5in}%
    \setlength\paperwidth  {7.25in}}
\DeclareOption{landscape}
   {\setlength\@tempdima   {\paperheight}%
    \setlength\paperheight {\paperwidth}%
    \setlength\paperwidth  {\@tempdima}}
\DeclareOption{10pt}{\renewcommand\@ptsize{0}}
\DeclareOption{11pt}{\renewcommand\@ptsize{1}}
\DeclareOption{12pt}{\renewcommand\@ptsize{2}}
\DeclareOption{twoside}{\@twosidetrue  \@mparswitchtrue}
\DeclareOption{draft}{\setlength\overfullrule{5pt}}
\DeclareOption{final}{\setlength\overfullrule{0pt}}
\DeclareOption{notitlepage}{\@titlepagefalse}
\DeclareOption{onecolumn}{\@twocolumnfalse}
\DeclareOption{twocolumn}{\@twocolumntrue}
\DeclareOption{leqno}{\input{leqno.clo}}
\DeclareOption{subeqn}{\input{subeqn.clo}}
\DeclareOption{oneeqnum}{\@oneeqnumtrue} % added 7.19.96
\DeclareOption{onetabnum}{\@onetabnumtrue} % added 7.19.96
\DeclareOption{onefignum}{\@onefignumtrue} % added 7.19.96
\DeclareOption{onethmnum}{\@onethmnumtrue} % added 7.29.96
\DeclareOption{translated}{\@translatedtrue} % jan 7 2004
%\DeclareOption{openbib}{\@openbibtrue}
\ExecuteOptions{letterpaper,10pt,twoside,onecolumn,leqno,draft,notitlepage}
\ProcessOptions
\input{siam1\@ptsize.clo}
\setlength\lineskip{1\p@}
\setlength\normallineskip{1\p@}
\renewcommand\baselinestretch{}
\setlength\parskip{0\p@ \@plus \p@}
\@lowpenalty   51
\@medpenalty  151
\@highpenalty 301
\setcounter{topnumber}{2}
\renewcommand\topfraction{.9}
\setcounter{bottomnumber}{1}
\renewcommand\bottomfraction{.1}
\setcounter{totalnumber}{3}
\renewcommand\textfraction{.1}
\renewcommand\floatpagefraction{.91}
\setcounter{dbltopnumber}{2}
\renewcommand\dbltopfraction{.7}
\renewcommand\dblfloatpagefraction{.5}
\renewcommand{\ps@plain}{\let\@mkboth\@gobbletwo%
  \renewcommand{\@oddhead}{}%
  \renewcommand{\@evenhead}{}%
  \renewcommand{\@evenfoot}{\hfil\footnotesize\textrm{\thepage}\hfil}%
  \renewcommand{\@oddfoot}{\@evenfoot}}

    \def\ps@headings{%
      \let\@oddfoot\@empty\let\@evenfoot\@empty
      \def\@evenhead{\rlap{\thepage}\hfil\upshape\footnotesize\leftmark\hfil}%          %!
      \def\@oddhead{\hbox{}\hfil{\upshape\footnotesize\rightmark}\hfil\llap{\thepage}}% %!
      \let\@mkboth\markboth
      \def\sectionmark##1{%
        \markboth {\uppercase{\ifnum \c@secnumdepth >\z@
            \thesection.\hskip 1em\relax\fi
            ##1}}{}}%
      \def\subsectionmark##1{%
        \markright {\ifnum \c@secnumdepth >\@ne
            \thesubsection\hskip 1em\relax \fi
            ##1}}}

\def\ps@myheadings{%
    \let\@oddfoot\@empty\let\@evenfoot\@empty
    \def\@evenhead{\rlap{\thepage}\hfil\upshape\footnotesize\leftmark\hfil}%          %!
    \def\@oddhead{\hbox{}\hfil{\upshape\footnotesize\rightmark}\hfil\llap{\thepage}}% %!
    \let\@mkboth\@gobbletwo
    \let\sectionmark\@gobble
    \let\subsectionmark\@gobble
    }


\newcommand\maketitle{\par
  \begingroup
    \renewcommand{\thefootnote}{\fnsymbol{footnote}}%
    \def\@makefnmark{\hbox to\z@{$\m@th^{\@thefnmark}$\hss}}%
    \long\def\@makefntext##1{\parindent 1em\noindent
            \hbox to1.8em{\hss$\m@th^{\@thefnmark}$}##1}%
    \if@twocolumn
      \ifnum \col@number=\@ne
        \@maketitle
      \else
        \twocolumn[\@maketitle]%
      \fi
    \else
      \global\@topnum\z@   % Prevents figures from going at top of page.
      \@maketitle
    \fi
    \thispagestyle{plain}\@thanks
  \endgroup
  \setcounter{footnote}{0}%
  \let\maketitle\relax\let\@maketitle\relax
  \gdef\@thanks{}\gdef\@author{}\gdef\@title{}\let\thanks\relax}
%_%_%_%_%
%_%_%_%_% Macros for subtitle (subauthor?), altered slugline/slugger for translated version
%_%_%_%_%
\long\def\subtitle#1{\gdef\@subtitle{\par\vskip8pt\footnotesize#1}}
\def\@subtitle{}
%
\long\def\supertitle#1{\gdef\@supertitle{\par\bfseries#1\vskip17.5pt\par}}
\def\@supertitle{}
%_%_%_%_%
%_%_%_%_%
%_%_%_%_%
%
\def\@translation{}
%
\def\slugger#1#2#3#4#5{\gdef\@slugger{\thispagestyle{plain}%
\vspace*{-36pt}
{\sixptsize\baselineskip10pt
\noindent
\expandafter\csname#1\endcsname.\hspace*{\fill}
{\scriptsize{\copyright}} #2 Society for Industrial and
Applied\vspace*{-1.2mm}  Mathematics\\
Vol.\ #3, No.\ #4, pp.\ #5
\hspace*{\fill} \@translation\par}
\normalsize\vskip19.7pt}}
%
\if@translated
\newcommand\tpa{T{\fiveptsize HEORY}~P{\fiveptsize ROBAB.}~A{\fiveptsize PPL}}% added 1/7/04
\def\@translation{Translated from Russian Journal}  
\else%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand\tpa{T{\fiveptsize HEORY}~P{\fiveptsize ROBAB.}~A{\fiveptsize PPL}}% added 1/7/04  
\fi
%
\def\@slugger{}
\def\@slugline{}
%_%_%_%_%
%_%_%_%_%
%_%_%_%_%
\def\@maketitle{%
  \null
\@slugger
  \begin{center}%
\@supertitle%
    {\bfseries\@ucnothanks\@title\par}%
    \vskip .075in%
    {\footnotesize
      \spaceskip=1.5\fontdimen2\the\font
      \def\and{\ \scriptsize AND }
      \@tempswafalse\expandafter\@doauth\@author\and\relax}%
\@subtitle%
  \end{center}%
  \par
  \vskip .11in}
\def\@ucnothanks#1{\expandafter\@ucnt#1\thanks\relax}
\def\@ucnt#1\thanks{\uppercase{#1}\futurelet\@tempa\@ucnta}
\def\@ucnta{\ifx\@tempa\relax\else\@ucntb\fi}
\def\@ucntb#1\thanks\relax{\thanks{#1}}
\def\@doauth#1\and{\let\@nextdoa=\@doauth
 \def\@tempc{\@ucnothanks{#1}}
 \futurelet\@tempa\@doautha}
\def\@doautha{\ifx\@tempa\relax
  \if@tempswa {\and}\fi
  \let\@nextdoa=\relax
 \else
  \if@tempswa \gdef\and{,\ \scriptsize AND }, \fi
 \fi
 \@tempc\unskip\@tempswatrue\@nextdoa}
\let\and=\relax

\newcommand{\sixptsize}{%
   \@setfontsize\sixptsize{6}{8}}

%%create five-point size
\newcommand{\fiveptsize}{%
   \@setfontsize\fiveptsize{5}{7}}


\newcommand\simac{SIAM J{\fiveptsize OURNAL} M{\fiveptsize ACRO}}
\newcommand\siap{SIAM J.\ A{\fiveptsize PPL.} M{\fiveptsize ATH}}
\newcommand\sicomp{SIAM J.\ C{\fiveptsize OMPUT}}
\newcommand\sicon{SIAM J.\ C{\fiveptsize ONTROL}  O{\fiveptsize PTIM}}
\newcommand\sidma{SIAM J.\ D{\fiveptsize ISCRETE} M{\fiveptsize ATH}}
\newcommand\sima{SIAM J.\ M{\fiveptsize ATH.} A{\fiveptsize NAL}}
\newcommand\simax{SIAM J.\ M{\fiveptsize ATRIX} A{\fiveptsize NAL.} A{\fiveptsize PPL}}
\newcommand\sinum{SIAM J.\ N{\fiveptsize UMER.} A{\fiveptsize NAL}}
\newcommand\siopt{SIAM J.\ O{\fiveptsize PTIM}}
\newcommand\sisc{SIAM J.\ S{\fiveptsize CI.} C{\fiveptsize OMPUT}}
\newcommand\sirev{SIAM R{\fiveptsize EV}}
\newcommand\mms{M{\fiveptsize ULTISCALE}~M{\fiveptsize ODEL.}~S{\fiveptsize IMUL}} % Added 9/17/02  
   
       
\setcounter{secnumdepth}{3}
\newcounter {section}
\newcounter {subsection}[section]
\newcounter {subsubsection}[subsection]
\newcounter {paragraph}[subsubsection]
\newcounter {subparagraph}[paragraph]
\renewcommand\thesection       {\arabic{section}}
\renewcommand\thesubsection    {\thesection.\arabic{subsection}}
\renewcommand\thesubsubsection {\thesubsection.\arabic{subsubsection}}
\renewcommand\theparagraph     {\thesubsubsection.\arabic{paragraph}}
\renewcommand\thesubparagraph  {\theparagraph.\arabic{subparagraph}}


\def\@sect#1#2#3#4#5#6[#7]#8{\ifnum #2>\c@secnumdepth
     \def\@svsec{}\else
     \refstepcounter{#1}\edef\@svsec{\csname the#1\endcsname.\hskip .5em }\fi
     \@tempskipa #5\relax
      \ifdim \@tempskipa>\z@
        \begingroup #6\relax
          \@hangfrom{\hskip #3\relax\@svsec}{\interlinepenalty \@M #8\par}
        \endgroup
       \csname #1mark\endcsname{#7}\addcontentsline
         {toc}{#1}{\ifnum #2>\c@secnumdepth \else
                      \protect\numberline{\csname the#1\endcsname}\fi
                    #7}\else
        \def\@svsechd{#6\hskip #3\@svsec #8.\csname #1mark\endcsname
                      {#7}\addcontentsline
                           {toc}{#1}{\ifnum #2>\c@secnumdepth \else
                             \protect\numberline{\csname the#1\endcsname}\fi
                       #7}}\fi
     \@xsect{#5}}
\def\@ssect#1#2#3#4#5{\@tempskipa #3\relax
   \ifdim \@tempskipa>\z@
     \begingroup #4\@hangfrom{\hskip #1}{\interlinepenalty \@M
#5.\par}\endgroup
   \else \def\@svsechd{#4\hskip #1\relax #5.}\fi
    \@xsect{#3}}

             
\newcommand\section{\@startsection{section}{1}{.25in}%
                                   {1.3ex \@plus .5ex \@minus .2ex}%
                                   {-.5em \@plus -.1em}%
                                   {\reset@font\normalsize\bfseries}}
\newcommand\subsection{\@startsection{subsection}{2}{.25in}%
                                     {1.3ex\@plus .5ex \@minus .2ex}%
                                     {-.5em \@plus -.1em}%
                                     {\reset@font\normalsize\bfseries}}
\newcommand\subsubsection{\@startsection{subsubsection}{3}{.25in}%
                                     {1.3ex\@plus .5ex \@minus .2ex}%
                                     {-.5em \@plus -.1em}%
                                     {\reset@font\normalsize\bfseries}}
\newcommand\paragraph{\@startsection{paragraph}{4}{.25in}%
                                    {\parskip}%
                                    {-.5em plus -.1em}%
                                    {\reset@font\normalsize\itshape}}
\newcommand\subparagraph{\@startsection{subparagraph}{5}{\parindent}%
                                       {\parskip}%
                                       {-.5em plus -.1em}%
                                      {\reset@font\normalsize\itshape}}
\if@twocolumn
  \setlength\leftmargini  {2em}
\else
  \setlength\leftmargini  {0.5in}
\fi
\setlength\leftmarginii  {22pt}
\setlength\leftmarginiii {18.7pt}
\setlength\leftmarginiv  {17pt}
\if@twocolumn
  \setlength\leftmarginv  {.5em}
  \setlength\leftmarginvi {.5em}
\else
  \setlength\leftmarginv  {10pt}
  \setlength\leftmarginvi {10pt}
\fi
\setlength  \leftmargin{\leftmargini}
\setlength  \labelsep  {.5em}
\setlength  \labelwidth{\leftmargini}
\addtolength\labelwidth{-\labelsep}
\@beginparpenalty -\@lowpenalty
\@endparpenalty   -\@lowpenalty
\@itempenalty     -\@lowpenalty
\renewcommand\theenumi{\arabic{enumi}}
\renewcommand\theenumii{\alph{enumii}}
\renewcommand\theenumiii{\roman{enumiii}}
\renewcommand\theenumiv{\Alph{enumiv}}
\newcommand\labelenumi{\theenumi.}
\newcommand\labelenumii{(\theenumii)}
\newcommand\labelenumiii{\theenumiii.}
\newcommand\labelenumiv{\theenumiv.}
\renewcommand\p@enumii{\theenumi}
\renewcommand\p@enumiii{\theenumi\theenumii}
\renewcommand\p@enumiv{\p@enumiii\theenumiii}
\newcommand\labelitemi{$\m@th\bullet$}
\newcommand\labelitemii{\normalfont\bfseries --}
\newcommand\labelitemiii{$\m@th\ast$}
\newcommand\labelitemiv{$\m@th\cdot$}
\newenvironment{description}
               {\list{}{\labelwidth\z@ \itemindent-\leftmargin
                        \let\makelabel\descriptionlabel}}
               {\endlist}
\newcommand\descriptionlabel[1]{\hspace\labelsep
                                \normalfont\bfseries #1}
\newcounter{rmnum}
\newenvironment{romannum}
               {\begin{list}{{\upshape (\roman{rmnum})}}{\usecounter{rmnum}
                \setlength{\leftmargin}{0pt}
                \setlength{\itemindent}{42pt}}}{\end{list}}
\newcounter{muni}
\newenvironment{remunerate}
               {\begin{list}{{\upshape \arabic{muni}.}}{\usecounter{muni}
                \setlength{\leftmargin}{0pt}
                \setlength{\itemindent}{38pt}}}{\end{list}}
                               
\newenvironment{@abssec}[1]{%
     \if@twocolumn
       \section*{#1}%
     \else
       \vspace{.05in}\footnotesize
       \parindent .2in
         {\upshape\bfseries #1. }\ignorespaces
     \fi}
     {\if@twocolumn\else\par\vspace{.1in}\fi}

\newenvironment{@doisec}[1]{%
     \if@twocolumn
       \section*{#1}%
     \else
       \vspace{.05in}\footnotesize
       \parindent .2in
         {\upshape\bfseries #1. }\ignorespaces\ignorespaces
     \fi}
     {\if@twocolumn\else\par\vspace{.1in}\fi}

\newenvironment{abstract}{\begin{@abssec}{\abstractname}}{\end{@abssec}}
\newenvironment{keywords}{\begin{@abssec}{\keywordsname}}{\end{@abssec}}
\newenvironment{AMS}{\begin{@abssec}{\AMSname}}{\end{@abssec}}
\newenvironment{AM}{\begin{@abssec}{\AMname}}{\end{@abssec}}
%\newenvironment{PII}{\begin{@abssec}{\PIIname}}{\end{@abssec}}
\newenvironment{DOI}{\begin{@doisec}{\DOIname}}{\end{@doisec}}


\newenvironment{verse}
               {\let\\=\@centercr
                \list{}{\itemsep      \z@
                        \itemindent   -1.5em%
                        \listparindent\itemindent
                        \rightmargin  \leftmargin
                        \advance\leftmargin 1.5em}%
                \item[]}
               {\endlist}
\newenvironment{quotation}
               {\list{}{\listparindent 1.5em%
                        \itemindent    \listparindent
                        \rightmargin   \leftmargin
                        \parsep        \z@ \@plus\p@}%
                \item[]}
               {\endlist}
\newenvironment{quote}
               {\list{}{\rightmargin\leftmargin}%
                \item[]}
               {\endlist}
\def\@begintheorem#1#2{\par\bgroup{\scshape #1\ #2. }\it\ignorespaces}
\def\@opargbegintheorem#1#2#3{\par\bgroup%
   {\scshape #1\ #2\ ({\upshape #3}). }\it\ignorespaces}
\def\@endtheorem{\egroup}
\def\proof{\par{\it Proof}. \ignorespaces}

\def\endproof{\vbox{\hrule height0.6pt\hbox{%
   \vrule height1.3ex width0.6pt\hskip0.8ex
   \vrule width0.6pt}\hrule height0.6pt
  }}

\if@onethmnum
  \newtheorem{theorem}{Theorem}
  \newtheorem{lemma}[theorem]{Lemma}
  \newtheorem{corollary}[theorem]{Corollary}
  \newtheorem{proposition}[theorem]{Proposition}
  \newtheorem{definition}[theorem]{Definition}
\else
  \newtheorem{theorem}{Theorem}[section]
  \newtheorem{lemma}[theorem]{Lemma}
  \newtheorem{corollary}[theorem]{Corollary}
  \newtheorem{proposition}[theorem]{Proposition}
  \newtheorem{definition}[theorem]{Definition}
\fi


% FROM FIXUP.STY
% We now redefine the eqnarray environment to correct the space around
% the operator.   Any changes to the definition in LaTeX itself
% will cause the `Warning: unable...'
% message to appear.  If this happens it will be necessary to update the
% definition of  \@tempb below and incorperate the changes into
% the new definitions of \eqnarray.
 
 
% This is the current definition of \eqnarray for the fleqn document style
% latex.ltx
 
\def\@tempb{%
   \stepcounter{equation}%
   \def\@currentlabel{\p@equation\theequation}%
   \global\@eqnswtrue
   \m@th
   \global\@eqcnt\z@
   \tabskip\@centering
   \let\\\@eqncr
   $$\everycr{}\halign to\displaywidth\bgroup
       \hskip\@centering$\displaystyle\tabskip\z@skip{##}$\@eqnsel
      &\global\@eqcnt\@ne\hskip \tw@\arraycolsep \hfil${##}$\hfil
      &\global\@eqcnt\tw@ \hskip \tw@\arraycolsep
         $\displaystyle{##}$\hfil\tabskip\@centering
      &\global\@eqcnt\thr@@ \hb@xt@\z@\bgroup\hss##\egroup
         \tabskip\z@skip
      \cr
}
\ifx\eqnarray\@tempb    % Try the default eqnarray environment
  \def\eqnarray{%
   \stepcounter{equation}%
   \def\@currentlabel{\p@equation\theequation}%
   \global\@eqnswtrue
   \m@th
   \global\@eqcnt\z@
   \tabskip\@centering
   \let\\\@eqncr
   $$\everycr{}\halign to\displaywidth\bgroup
       \hskip\@centering$\displaystyle\tabskip\z@skip{##}$\@eqnsel
      &\global\@eqcnt\@ne \hfil$\displaystyle{{}##{}}$\hfil
      &\global\@eqcnt\tw@ $\displaystyle{##}$\hfil\tabskip\@centering
      &\global\@eqcnt\thr@@ \hb@xt@\z@\bgroup\hss##\egroup
         \tabskip\z@skip
      \cr
}
\else    \typeout{Warning: Unable to fix unknown version of \string\eqnarray.}
\fi
 
\def\@tempb{}


%% New Mathops.

\newcommand\const{\mathop{\operator@font const}\nolimits}
\newcommand\diag{\mathop{\operator@font diag}\nolimits}
\newcommand\grad{\mathop{\operator@font grad}\nolimits}
\newcommand\Range{\mathop{\operator@font Range}\nolimits}
\newcommand\rank{\mathop{\operator@font rank}\nolimits}
\newcommand\supp{\mathop{\operator@font supp}\nolimits}

\newcommand\appendix{%
\renewcommand{\section}{%
\secdef\append\sappend}%
 \setcounter{section}{0}%
 \setcounter{subsection}{0}%
 \renewcommand\thesection{\Alph{section}}}

\newcommand\Appendix{%
\renewcommand{\section}{%
\secdef\Append\sAppend}%
 \setcounter{section}{0}%
 \setcounter{subsection}{0}%
 \renewcommand\thesection{\Alph{section}}}

\newcommand\append[2][?]{%
\refstepcounter{section}%
{\vskip 1.3ex \@plus .5ex \@minus .2ex
\reset@font\normalsize\bfseries\appendixname\ \thesection. #2.}}

\newcommand\sappend[1]{%
\refstepcounter{section}
{\vskip 1.3ex \@plus .5ex \@minus .2ex
\reset@font\normalsize\bfseries\appendixname\ \thesection.}}

\newcommand\Append[2][?]{%
\refstepcounter{section}%
{\vskip 1.3ex \@plus .5ex \@minus .2ex
\reset@font\normalsize\bfseries\appendixname. #2.}}

\newcommand\sAppend[1]{%
\refstepcounter{section}
{\vskip 1.3ex \@plus .5ex \@minus .2ex
\reset@font\normalsize\bfseries\appendixname.}}

\setlength\arraycolsep{5\p@}
\setlength\tabcolsep{6\p@}
\setlength\arrayrulewidth{.4\p@}
\setlength\doublerulesep{2\p@}
\setlength\tabbingsep{\labelsep}
\skip\@mpfootins = \skip\footins
\setlength\fboxsep{3\p@}
\setlength\fboxrule{.4\p@}


\newcounter{figure}
\renewcommand\thefigure{\@arabic\c@figure}
\def\fps@figure{tp}
\def\ftype@figure{1}
\def\ext@figure{lof}
\def\fnum@figure{\figurename~\thefigure}
\newenvironment{figure}
               {\@float{figure}}
               {\end@float}
\newenvironment{figure*}
               {\@dblfloat{figure}}
               {\end@dblfloat}
\newcounter{table}
\renewcommand{\thetable}{\@arabic\c@table}
\def\fps@table{tp}
\def\ftype@table{2}
\def\ext@table{lot}
\def\fnum@table{\tablename~\thetable}
\newenvironment{table}
               {\@float{table}}
               {\end@float}
\newenvironment{table*}
               {\@dblfloat{table}}
               {\end@dblfloat}
\newlength\abovecaptionskip
\newlength\belowcaptionskip
\setlength\abovecaptionskip{10\p@}
\setlength\belowcaptionskip{10\p@}
\def\@figtxt{figure}
\long\def\@makecaption#1#2{%
    \footnotesize
    \setlength{\parindent}{1.5pc}
  \ifx\@captype\@figtxt
    \vskip\abovecaptionskip
    \setbox\@tempboxa\hbox{{\normalfont\scshape #1}. {\normalfont\itshape #2}}%
    \ifdim \wd\@tempboxa >\hsize
      {\normalfont\scshape #1}. {\normalfont\itshape #2}\par
    \else
      \global\@minipagefalse
      \hb@xt@\hsize{\hfil\box\@tempboxa\hfil}%
    \fi
  \else
    \hbox to\hsize{\hfil{\normalfont\scshape #1}\hfil}%
    \setbox\@tempboxa\hbox{{\normalfont\itshape #2}}%
    \ifdim \wd\@tempboxa >\hsize
      {\normalfont\itshape #2}\par
    \else
     \global\@minipagefalse
      \hb@xt@\hsize{\hfil\box\@tempboxa\hfil}%
    \fi
    \vskip\belowcaptionskip
  \fi}
\DeclareOldFontCommand{\rm}{\normalfont\rmfamily}{\mathrm}
\DeclareOldFontCommand{\sf}{\normalfont\sffamily}{\mathsf}
\DeclareOldFontCommand{\tt}{\normalfont\ttfamily}{\mathtt}
\DeclareOldFontCommand{\bf}{\normalfont\bfseries}{\mathbf}
\DeclareOldFontCommand{\it}{\normalfont\itshape}{\mathit}
\DeclareOldFontCommand{\sl}{\normalfont\slshape}{\@nomath\sl}
\DeclareOldFontCommand{\sc}{\normalfont\scshape}{\@nomath\sc}
\DeclareRobustCommand*\cal{\@fontswitch{\relax}{\mathcal}}
\DeclareRobustCommand*\mit{\@fontswitch{\relax}{\mathnormal}}
\newcommand\@pnumwidth{1.55em}
\newcommand\@tocrmarg {2.55em}
\newcommand\@dotsep{4.5}

\newdimen\bibindent
\bibindent=16pt
\newenvironment{thebibliography}[1]
     {\par\addvspace{.25in}
     \begin{center}
     \footnotesize\uppercase\expandafter{\refname}
     \end{center}
     \@mkboth{\uppercase\expandafter{\refname}}{\uppercase\expandafter{\refname}}
     \addvspace{.15in}\nopagebreak%
      \list{\@biblabel{\arabic{enumi}}}%
           {\settowidth\labelwidth{\@biblabel{#1}}%
            \leftmargin\labelwidth
            \advance\leftmargin\labelsep
%            \if@openbib
              \advance\leftmargin\bibindent
              \itemindent -\bibindent
              \listparindent \itemindent
              \parsep \z@
%            \fi
            \usecounter{enumi}%
            \let\p@enumi\@empty
            \renewcommand\theenumi{\arabic{enumi}}}%
%      \if@openbib
%        \renewcommand\newblock{\par}
%      \else
        \renewcommand\newblock{\hskip .11em \@plus.33em \@minus.07em}%
%      \fi
      \sloppy\clubpenalty4000\widowpenalty4000%
      \sfcode`\.=\@m\relax\footnotesize}
     {\def\@noitemerr
       {\@latex@warning{Empty `thebibliography' environment}}%
      \endlist}
\newcommand\newblock{}
\newenvironment{theindex}
               {\if@twocolumn
                  \@restonecolfalse
                \else
                  \@restonecoltrue
                \fi
                \columnseprule \z@
                \columnsep 35\p@
                \twocolumn[\section*{\indexname}]%
                \@mkboth{\uppercase{\indexname}}%
                        {\uppercase{\indexname}}%
                \thispagestyle{plain}\parindent\z@
                \parskip\z@ \@plus .3\p@\relax
                \let\item\@idxitem}
               {\if@restonecol\onecolumn\else\clearpage\fi}
\newcommand\@idxitem  {\par\hangindent 40\p@}
\newcommand\subitem   {\par\hangindent 40\p@ \hspace*{20\p@}}
\newcommand\subsubitem{\par\hangindent 40\p@ \hspace*{30\p@}}
\newcommand\indexspace{\par \vskip 10\p@ \@plus5\p@ \@minus3\p@\relax}
\renewcommand\footnoterule{%
  \kern-3\p@
  \hrule width .5in
  \kern 2.6\p@}
\long\def\@makefntext#1{%
    \parindent .25in%
    \noindent
    \hbox to .25in{\hss\@makefnmark}#1}
\newcommand\contentsname{Contents}
\newcommand\listfigurename{List of Figures}
\newcommand\listtablename{List of Tables}
\newcommand\refname{References}
\newcommand\indexname{Index}
\newcommand\figurename{Fig.}
\newcommand\tablename{Table}
\newcommand\partname{Part}
\newcommand\appendixname{Appendix}
\newcommand\abstractname{Abstract}
\newcommand\keywordsname{Key words}
\newcommand\AMSname{AMS subject classifications}
\newcommand\AMname{AMS subject classification}
%\newcommand\PIIname{PII}
\newcommand\DOIname{DOI}
\newcommand\URL{\protect\\ \hspace*{15.37pt}http://www.siam.org/journals/}
\newcommand\today{\ifcase\month\or
  January\or February\or March\or April\or May\or June\or
  July\or August\or September\or October\or November\or December\fi
  \space\number\day, \number\year}
\newcommand\sameauthor{\leavevmode\vrule height 2pt depth -1.6pt width 23pt}
\setlength\columnsep{10\p@}
\setlength\columnseprule{0\p@}
\pagestyle{plain}
\pagenumbering{arabic}      % Arabic page numbers

\if@compatibility%
\else
  \if@oneeqnum
  \else
     \@addtoreset{equation}{section}   %  \section resets 'equation' counter
     \renewcommand{\theequation}{\thesection.\arabic{equation}}  
  \fi
%
  \if@onefignum
  \else
    \@addtoreset{figure}{section}
    \renewcommand{\thefigure}{\thesection.\@arabic\c@figure}
  \fi
%
  \if@onetabnum
  \else
    \@addtoreset{table}{section}
    \renewcommand{\thetable}{\thesection.\@arabic\c@table}
  \fi
%
  \if@onethmnum
  \else
    \@addtoreset{theorem}{section}
    \renewcommand{\thetheorem}{\thesection.\arabic{theorem}}
  \fi
\fi

\onecolumn

\gdef\@siamlabel@error#1#2{%
   \GenericError{%
      \space\space\space\@spaces\@spaces\@spaces
   }{%
      SIAM Label Error: #1%
   }{%
      Correct multiply-defined labels.%
   }{#2}%
}

%%% NEW -- causes multiply defined labels to generate errors
\def\@newl@bel#1#2#3{%
  \@ifundefined{#1@#2}%
    \relax
    {\gdef \@multiplelabels {%
      \@latex@warning@no@line{Label `#2' multiply defined}}%
      \@siamlabel@error{There were multiply-defined labels}{}}%
  \global\@namedef{#1@#2}{#3}}
\def\newlabel{\@newl@bel r}
\@onlypreamble\@newl@bel
\let \@multiplelabels \relax
\def\label#1{\@bsphack
  \protected@write\@auxout{}%
         {\string\newlabel{#1}{{\@currentlabel}{\thepage}}}%
  \@esphack}
\def\refstepcounter#1{\stepcounter{#1}%
    \protected@edef\@currentlabel
       {\csname p@#1\endcsname\csname the#1\endcsname}%
}
%%%



\def\newarticle{\input{newart.tex}}

\endinput
%%
%% End of file `siamltex.cls'.


