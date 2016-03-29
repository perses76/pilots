<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:ext="rebelrunner.xsd" 
    xmlns="skeleton.xsd" 
    >
    <xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes"/>


    <xsl:template match="@*|*">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="ext:Footer">
        <block name="Footer">
            <xsl:apply-templates select="*" />
        </block>
    </xsl:template>

    <xsl:template match="ext:list|ext:list_item">
        <xsl:apply-templates select="*" />
    </xsl:template>

    <xsl:template match="ext:list_item/ext:link">
        <a class="footer-menu__link" href="{ @href }" target="{ @target }">
            <xsl:value-of select="." />
        </a>
    </xsl:template>

</xsl:stylesheet>
